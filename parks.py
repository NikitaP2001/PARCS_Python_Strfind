from Pyro4 import expose
import random


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers
        print("Inited")

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))

        (a, b) = self.read_input()
        batch_size = len(a) // len(self.workers)        

        # map
        mapped = []
        pos = 0
        end = 0
        for i in range(0, len(self.workers)):
            print("map %d" % i)
            beg = i * batch_size
            if i == len(self.workers) - 1:            
                end = len(a)
            else:
                end = min(len(a) - 1, (i + 1) * batch_size + len(b) - 1)
            if end - beg + 1 >= len(b):
                mapped.append(self.workers[i].mymap(a[beg:end], b, beg))

        all_pos = self.myreduce(mapped)

        self.write_output(all_pos)

        print("Job Finished")

    @staticmethod
    @expose
    def mymap(a, b, i):
        print(a, b, i)        

        entries = []

        for ic, c in enumerate(a):
            if len(a) - ic < len(b):
                break
            if a[ic:ic+len(b)] == b:
                entries.append(i + ic)

        return entries

    @staticmethod
    @expose
    def myreduce(mapped):
        print("reduce")
        output = []

        for pos in mapped:
            print("reduce loop")
            output = output + pos.value
        print("reduce done")
        return output

    def read_input(self):
        f = open(self.input_file_name, 'r')
        a = f.readline()
        b = f.readline()
        f.close()
        return a, b

    def write_output(self, output):
        f = open(self.output_file_name, 'w')
        f.write(', '.join((map(str, output))))
        f.write('\n')
        f.close()
        print("output done")     
