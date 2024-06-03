// necessary to convert vector
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "math.h"
#include "matrix.h"

PYBIND11_MODULE(myapp, myapp) {
    // interface for the matrix type enum
    pybind11::enum_<matrix::DummyMatrixType>(myapp, "DummyMatrixType")
        .value("DENSE", matrix::DummyMatrixType::DENSE)
        .value("SPARSE", matrix::DummyMatrixType::SPARSE)
        .value("UNKNOWN", matrix::DummyMatrixType::UNKNOWN)
        .export_values();

    // interface for the dummy matrix class
    pybind11::class_<matrix::DummyMatrix>(myapp, "DummyMatrix")
        .def(pybind11::init<>())
        .def_readwrite("rows", &matrix::DummyMatrix::rows)
        .def_readwrite("cols", &matrix::DummyMatrix::cols)
        .def_readwrite("type", &matrix::DummyMatrix::type)
        .def_property("data", &matrix::DummyMatrix::GetData,
                      &matrix::DummyMatrix::SetData);

    // submodule defining basic matrix math functions
    pybind11::module_ math = myapp.def_submodule("math", "Matrix Math Methods");
    math.def("Add", matrix::math::Add);
    math.def("Subtract", matrix::math::Subtract);
    math.def("Multiply", matrix::math::Multiply);
}