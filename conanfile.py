from conans import ConanFile, CMake, tools


class LibnoiseConan(ConanFile):
    name = "libnoise-conan"
    version = "0.1"
    no_copy_source = True

    def source(self):
        self.run("git clone git@github.com:qknight/libnoise.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="libnoise")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="libnoise/src")
        self.copy("*.h", dst="include", src="libnoise/noiseutils")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["noise", "noiseutils"]
