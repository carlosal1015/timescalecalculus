#!/usr/bin/env python
"""Taken from http://timescalewiki.org/index.php/Timescalecalculus_python_library_documentation
"""
from timescalecalculus import timescale as tsc


ts = tsc([2, 3, 5, 7, 11, 13, 17], 'primes')

print(ts.dexp_p(lambda x: 1, 5, 2))

print(ts.dexp_p(lambda x: 1, 11, 2))

print(ts.dexp_p(lambda x: x, 5, 2))
