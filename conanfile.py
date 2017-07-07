from conans import ConanFile, CMake


class BeaglerelayConan(ConanFile):
    name = "BeagleRelay"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/uilianries/BeagleRelay"
    description = "Relay manager for BeagleBoneBlack"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt"
    requires = "BeagleBoneBlackGPIO/0.2.0@uilianries/stable", "Poco/1.7.8p3@pocoproject/stable"
    default_options = "BeagleBoneBlackGPIO:shared=True", "Poco:shared=True"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("beagle-relay", dst="bin", src="bin")
