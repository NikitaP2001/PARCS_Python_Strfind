#include "chrgen.h"

RandomCharGenerator::RandomCharGenerator()
	: m_rnd(m_dev()),
	m_distc('a', 'z')
{
}

char RandomCharGenerator::generate()
{
	return m_distc(m_rnd);
}

void RandomCharGenerator::genStr(std::size_t length, std::string &outStr)
{
        outStr.clear();
	for (std::size_t i = 0; i < length; i++)
		outStr += generate();
}
