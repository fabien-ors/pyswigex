#include <iostream>
#include <vector>

/**
 * Write Fibonacci series up to n
 * @param n  Positive Integer
 */
void fib(int n)
{
  int a = 0;
  int b = 1;
  while (a < n)
  {
    std::cout << a << " ";
    a = b;
    b = a+b;
  }
  std::cout << std::endl;
}

/**
 * Return Fibonacci series up to n
 * @param n  Positive Integer
 */
std::vector<double> fib2(int n)
{
  std::vector<double> res;
  int a = 0;
  int b = 1;
  while (a < n)
  {
    res.push_back(a);
    a = b;
    b = a+b;
  }
  return res;
}
