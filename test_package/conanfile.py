from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "uilianries")


class BeaglerelayTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "BeagleRelay/0.1.0@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*", dst="bin", src="bin")

    def test(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.test()
