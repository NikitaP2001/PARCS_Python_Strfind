#include <memory>
#include <random>

class RandomCharGenerator {

public:
	RandomCharGenerator();

	
	char generate();

	void genStr(std::size_t length, std::string &outStr);

private:
	std::random_device m_dev;
	std::mt19937 m_rnd;
	std::uniform_int_distribution<std::mt19937::result_type> m_distc;
};
