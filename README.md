# InterlacingSequences
Some Python code to support MMath project on interlacing Fibonacci and Lucas sequences, specifically relating to series sums. 

Various functions are defined, some of which find terms of the 2 and 3 dimensional interlacing sequences (interlacing_fib_sequences and interlacing_fib_sequences2). Using these, we define a function (first_r_terms_sequence_powers) to iterate through and find the first r terms of the terms of the sequences to given powers and return them in a list. Using these, we can use the python function sum() to find the float (decimal approximation) of the sum of the first r terms in the sequence to given powers. Finally, using the Fraction module we can find fractions which approximate these floats. A small example shown below to illustrate how the code was used in the project to approximate the sums to infinity of the 2 dimensional interlacing sequence to powers of 4:

```python
>>> iterated_sum1 = sum(first_r_terms_sequence_powers(1, 10000, 4))
>>> print(Fraction(iterated_sum).limit_denominator(max_denominator=10000000))
>>> iterated_sum2 = sum(first_r_terms_sequence_powers(2, 10000, 4))
>>> print(Fraction(iterated_sum).limit_denominator(max_denominator=10000000))
17060625/994004
2575625/994004
```
