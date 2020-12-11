#!/usr/bin/env python
"""Taken from http://timescalewiki.org/index.php/Timescalecalculus_python_library_documentation
"""
from timescalecalculus import timescale as tsc
from fractions import Fraction


ts = tsc([0, Fraction(1, 3), Fraction(1, 2), Fraction(
    7, 9), 1, 2, 3, 4, 5, 6, 7], 'documentation example')

print(ts.name)
print(ts.sigma(0))
print(ts.sigma(4))
print(ts.sigma(7))

print(ts.mu(Fraction(1, 3)))

print(ts.rho(1))
print(ts.rho(3))
print(ts.rho(0))

print(ts.nu(Fraction(7, 9)))

print(ts.dderivative(lambda x: 1, 5))
print(ts.dderivative(lambda x: x*x, 5))

print(ts.dexp_p(lambda x: 1, 3, 1))
