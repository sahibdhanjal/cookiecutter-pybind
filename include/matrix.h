#pragma once

#include <iostream>
#include <vector>

namespace matrix {

// Designate a matrix as sparse, dense or unknown if unspecified
enum DummyMatrixType { DENSE, SPARSE, UNKNOWN };

// simple matrix struct for this example
struct DummyMatrix {
    std::vector<std::vector<int>> data;
    size_t rows;
    size_t cols;
    DummyMatrixType type;

    void SetData(const std::vector<std::vector<int>>& data) {
        this->rows = data.size();
        this->cols = data.size() ? data[0].size() : 0;
        this->data = data;
    }

    std::vector<std::vector<int>> GetData() { return this->data; }
};

}  // namespace matrix
