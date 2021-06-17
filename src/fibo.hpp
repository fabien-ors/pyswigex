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
    int aa = a;
    a = b;
    b = aa+b;
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
    int aa = a;
    a = b;
    b = aa+b;
  }
  return res;
}
