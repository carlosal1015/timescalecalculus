#!/usr/bin/env python
"""Taken from http://timescalewiki.org/index.php/Timescalecalculus_python_library_documentation
"""
from timescalecalculus import timescale as tsc


ts = tsc([1, 2, 3, 4, 5])

print(ts.dexp_p(lambda x: 1, 3, 1))
print(ts.dexp_p(lambda x: 2, 3, 1))
print(ts.dexp_p(lambda x: x, 3, 1))

print(ts.dexp_p(lambda x: ts.dexp_p(lambda x: 1, x, 1), 4, 1))
