cmake_minimum_required(VERSION 3.2)

set(CMAKE_C_COMPILER /usr/bin/gcc)
set(CMAKE_CXX_COMPILER /usr/bin/g++)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS ON)

project(myapp)

# you can add system installed modules as follows
# find_package(Ceres REQUIRED)

# or if they need to be built locally, install them using
add_subdirectory(third-party/pybind11)

# add all functions you want for compilation as follows
pybind11_add_module(myapp
    src/header_impl.cpp
)

# add the include directory to pull headers for compilation
target_include_directories(myapp
    PUBLIC
    include
)

# add any other library you might need here as shown
target_link_libraries(myapp
    PRIVATE
    # Ceres::ceres
)
