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
    default_options = "BeagleBoneBlackGPIO:shared=True", "Poco:shared=True",
    "Poco:enable_net=False", "Poco:enable_mongodb=False", "Poco:enable_data_sqlite=False"
    "Poco:enable_netssl=False", "Poco:enable_netssl_win=False", "Poco:enable_util=False",
    "Poco:enable_xml=False", "Poco:force_openssl=False", "Poco:enable_zip=False",
    "Poco:enable_json=False", "Poco:enable_crypto=False", "Poco:enable_data=False"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("beagle-relay", dst="bin", src="bin")
