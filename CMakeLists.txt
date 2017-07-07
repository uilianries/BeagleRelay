cmake_minimum_required(VERSION 2.8)
project(beagle-relay CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(src)
