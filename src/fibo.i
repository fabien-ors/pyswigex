%module fibo

// Turn on auto-generated docstrings
%feature("autodoc", "1");

%include std_vector.i

// Commandes for generating python3 wrapper 
// swig -c++ -python -o fibo_wrap.cpp fibo.i
// g++ -std=c++11 -fpic -shared fibo_wrap.cpp `python3-config --cflags` `python3-config --ldflags --embed` -o _fibo.so

%template(VectorDouble) std::vector<double>;

%include fibo.hpp

%{
  #include "fibo.hpp"
%}

