from __future__ import annotations

import myapp


# Python based matrix interface which can be used to convert a DummyMatrix
# defined in Python to one in C++ using a c_obj. This is not necessary to
# implement and is shown here primarily to showcase the difference in
# performance of C++ library vs a Python library
class PyDummyMatrix:
    def __init__(self, data=[], type=myapp.DummyMatrixType.UNKNOWN):
        self._data = data
        self._rows = len(data)
        self._cols = len(data[0]) if len(data) else 0
        self._type = type

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def type(self):
        return self._type

    @property
    def data(self):
        return self._data

    @property
    def c_obj(self):
        obj = myapp.DummyMatrix()
        obj.rows = self._rows
        obj.cols = self._cols
        obj.type = self._type
        obj.data = self._data
        return obj

    def __str__(self):
        out = ""
        for i in range(self._rows):
            out += (
                " ".join(str(self._data[i][x]) for x in range(self._cols))
                + "\n"
            )
        return out


def Add(a, b):
    if a.rows == b.rows and a.cols == b.cols:
        result = [[0 for _ in range(a.cols)] for _ in range(a.rows)]
        for i in range(a.rows):
            for j in range(a.cols):
                result[i][j] = a.data[i][j] + b.data[i][j]
        return PyDummyMatrix(result)
    print("Failed to add both matrices")
    return PyDummyMatrix()


def Subtract(a, b):
    if a.rows == b.rows and a.cols == b.cols:
        result = [[0 for _ in range(a.cols)] for _ in range(a.rows)]
        for i in range(a.rows):
            for j in range(a.cols):
                result[i][j] = a.data[i][j] - b.data[i][j]
        return PyDummyMatrix(result)
    print("Failed to subtract both matrices")
    return PyDummyMatrix()


def Multiply(a, b):
    if a.cols == b.rows:
        result = [[0 for _ in range(b.cols)] for _ in range(a.rows)]
        for i in range(a.rows):
            for j in range(b.cols):
                for k in range(a.cols):
                    result[i][j] += a.data[i][k] * b.data[k][j]
        return PyDummyMatrix(result)
    print("Failed to multiply both matrices")
    return PyDummyMatrix()
