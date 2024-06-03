cmake_minimum_required(VERSION 2.6)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS ON)

project(myapp)

# you can add system installed modules as follows
# find_package(Ceres REQUIRED)

# or if they need to be built locally, install them using
add_subdirectory(third-party/pybind11)

# add all functions you want for compilation as follows
pybind11_add_module(myapp
    src/interface.cpp
    src/math.cpp
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
