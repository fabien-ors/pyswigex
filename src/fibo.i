%module fibo

// https://stackoverflow.com/a/26035360/3952924
%import "documentation.i"

%include std_vector.i
%include std_string.i

%template(VectorInt) std::vector<int>;

%include fibo.hpp

%{
  #include "fibo.hpp"
%}

