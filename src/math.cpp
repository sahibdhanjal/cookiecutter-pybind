#include "math.h"

namespace matrix {
namespace math {

std::tuple<bool, DummyMatrix> Add(const DummyMatrix& a, const DummyMatrix& b) {
    if (a.rows == b.rows && a.cols == b.cols) {
        DummyMatrix output;
        std::vector<std::vector<int>> result(a.rows,
                                             std::vector<int>(a.cols, 0));
        for (size_t row = 0; row < a.rows; row++)
            for (size_t col = 0; col < a.cols; col++)
                result[row][col] = a.data[row][col] + b.data[row][col];
        output.SetData(result);
        return {true, output};
    }
    return {false, DummyMatrix()};
}

std::tuple<bool, DummyMatrix> Subtract(const DummyMatrix& a,
                                       const DummyMatrix& b) {
    if (a.rows == b.rows && a.cols == b.cols) {
        DummyMatrix output;
        std::vector<std::vector<int>> result(a.rows,
                                             std::vector<int>(a.cols, 0));
        for (size_t row = 0; row < a.rows; row++)
            for (size_t col = 0; col < a.cols; col++)
                result[row][col] = a.data[row][col] - b.data[row][col];
        output.SetData(result);
        return {true, output};
    }
    return {false, DummyMatrix()};
}

std::tuple<bool, DummyMatrix> Multiply(const DummyMatrix& a,
                                       const DummyMatrix& b) {
    if (a.cols == b.rows) {
        DummyMatrix output;
        std::vector<std::vector<int>> result(a.rows,
                                             std::vector<int>(b.cols, 0));
        for (size_t row = 0; row < a.rows; row++)
            for (size_t col = 0; col < b.cols; col++)
                for (size_t k = 0; k < a.cols; k++)
                    result[row][col] += a.data[row][k] * b.data[k][col];
        output.SetData(result);
        return {true, output};
    }
    return {false, DummyMatrix()};
}

}  // namespace math
}  // namespace matrix