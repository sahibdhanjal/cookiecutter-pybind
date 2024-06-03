#pragma once

#include <tuple>

#include "matrix.h"

namespace matrix {
namespace math {

// simple matrix math functions
std::tuple<bool, DummyMatrix> Add(const DummyMatrix& a, const DummyMatrix& b);
std::tuple<bool, DummyMatrix> Subtract(const DummyMatrix& a,
                                       const DummyMatrix& b);
std::tuple<bool, DummyMatrix> Multiply(const DummyMatrix& a,
                                       const DummyMatrix& b);

}  // namespace math
}  // namespace matrix