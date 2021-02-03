from conans import ConanFile, CMake, tools


class LibnoiseConan(ConanFile):
    name = "libnoise-conan"
    version = "0.1"
    no_copy_source = True

    def source(self):
        self.run("git clone git@github.com:qknight/libnoise.git")

    def package(self):
        self.copy("*.h", dst="include", src="libnoise/src/noise")
