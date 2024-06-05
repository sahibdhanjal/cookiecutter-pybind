from __future__ import annotations

import time

import myapp.math as Math  # c++ binding for math functions
import numpy as np
from myapp import DummyMatrix as Mat  # c++ binding of matrix

from app.matrix import Add
from app.matrix import Multiply
from app.matrix import PyDummyMatrix as pyMat  # python matrix
from app.matrix import Subtract


def AddPyBind(a, b):
    success, result = Math.Add(a, b)
    if not success:
        print("Failed to add both matrices")
    return result


def SubtractPyBind(a, b):
    success, result = Math.Subtract(a, b)
    if not success:
        print("Failed to subtract both matrices")
    return result


def MultiplyPyBind(a, b):
    success, result = Math.Multiply(a, b)
    if not success:
        print("Failed to multiply both matrices")
    return result


def TestAdd(a, b):
    pyA, pyB = pyMat(a), pyMat(b)
    t0 = time.time()
    pyRes = Add(pyA, pyB)
    t1 = time.time()
    cppRes = AddPyBind(pyA.c_obj, pyB.c_obj)
    t2 = time.time()
    print(f"Addition: Python: {t1-t0}, Binding: {t2-t1}")
    return pyRes.data == cppRes.data


def TestSubtract(a, b):
    pyA, pyB = pyMat(a), pyMat(b)
    t0 = time.time()
    pyRes = Subtract(pyA, pyB)
    t1 = time.time()
    cppRes = SubtractPyBind(pyA.c_obj, pyB.c_obj)
    t2 = time.time()
    print(f"Subtraction: Python: {t1-t0}, Binding: {t2-t1}")
    return pyRes.data == cppRes.data


def TestMultiply(a, b):
    pyA, pyB = pyMat(a), pyMat(b)
    t0 = time.time()
    pyRes = Multiply(pyA, pyB)
    t1 = time.time()
    cppRes = MultiplyPyBind(pyA.c_obj, pyB.c_obj)
    t2 = time.time()
    print(f"Multiplication: Python: {t1-t0}, Binding: {t2-t1}")
    return pyRes.data == cppRes.data


def TestEquivalence(a):
    pyA = pyMat(a)
    cppA = Mat()
    cppA.data = a
    return type(pyA) is pyMat and type(cppA) is Mat and pyA.data == cppA.data


def TimeAndTestFunctions():
    rows, cols = 100, 100
    low, high = -1000, 1000
    a = np.random.randint(low, high, (rows, cols)).tolist()
    b = np.random.randint(low, high, (rows, cols)).tolist()
    # test both pythonic implementation, c++ implementation
    # and the equivalence of python and c++
    assert TestEquivalence(a)
    assert TestAdd(a, b)
    assert TestSubtract(a, b)
    assert TestMultiply(a, b)


if __name__ == "__main__":
    TimeAndTestFunctions()
