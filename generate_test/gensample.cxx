#include <iostream>
#include <fstream>
#include <cstring>

#include "chrgen.h"

int main(int argc, char *argv[])
{
        RandomCharGenerator gen;
        if (argc != 3) {
                std::cout << "[-] wrong args count" << std::endl;
                exit(1);
        }

        std::size_t sampleSize = atoi(argv[1]);
        std::string searchStr = argv[2];
        std::string sampleName = "sample_" + std::to_string(sampleSize) + ".txt";

        std::ofstream fout(sampleName, std::ios::out | std::ios::binary);


        std::cout << "[i] generating " << sampleSize / 1000 
        << " 1000 size smpls" << std::endl;
        std::string buffer;
        for (std::size_t i = 0; i < sampleSize / 1000; i++) {
                gen.genStr(1000, buffer);
                fout.write(buffer.c_str(), buffer.size());
        }
        fout << std::endl << searchStr;
        std::cout << "[+] completed" << std::endl;
}
