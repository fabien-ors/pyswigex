%module fibo

// Turn on auto-generated docstrings
%feature("autodoc", "1");

%include std_vector.i
%include std_string.i

// Commandes for generating python3 wrapper 
// swig -c++ -python -o fibo_wrap.cpp fibo.i
// g++ -std=c++11 -fpic -shared *.cpp `python3-config --cflags` `python3-config --ldflags --embed` -o _fibo.so

%template(VectorInt) std::vector<int>;

%include fibo.hpp

%{
  #include "fibo.hpp"
%}

