#include "fibo.hpp"
#include <iostream>

/**
 * Default constructor of a class which handle Fibonacci integer serie up to n
 * 
 * @param n     Strict Positive Integer
 * @param title Title to be printed
 */
Fibo::Fibo(int n, const std::string& title)
: _n(n)
, _title(title)
{
  if (_n <= 0)
  {
    std::cout << "Fibonacci class must be initialized with a strict positive integer. N is set to 50." << std::endl;
    _n = 50;
  }
  if (_title.empty())
  {
    _title = "Fibonacci";
  }
}

/**
 * Destructor
 */
Fibo::~Fibo()
{
}

/**
 * Write the Fibonacci serie to standard output
 *
 * @param showTitle Flag for displaying title
 */
void Fibo::display(bool showTitle) const
{
  int a = 0;
  int b = 1;
  if (showTitle) std::cout << _title << ": ";
  while (a < _n)
  {
    std::cout << a << " ";
    int aa = a;
    a = b;
    b = aa+b;
  }
  std::cout << std::endl;
}

/**
 * Return the Fibonacci serie as a vector of integer
 *
 * @return Fibonacci integer vector serie
 */
std::vector<int> Fibo::get() const
{
  std::vector<int> res;
  int a = 0;
  int b = 1;
  while (a < _n)
  {
    res.push_back(a);
    int aa = a;
    a = b;
    b = aa+b;
  }
  return res;
}
