import subprocess

from setuptools import Command, find_packages, setup


class SimpleCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Hello World!")


class VetCommand(SimpleCommand):
    description = "Run vet on code"

    def run(self):
        print("Running vet...")
        subprocess.check_call(["pflake8", "flaskr"])


class FmtCommand(SimpleCommand):
    description = "Format code with black"

    def run(self):
        subprocess.check_call(["isort", "flaskr"])
        subprocess.check_call(["black", "flaskr"])


class ServerCommand(SimpleCommand):
    description = "Run the server"

    def run(self):
        from flaskr import create_app

        create_app(
            test_config={
                "DEBUG": True,
            }
        ).run()


setup(
    name="flaskr",
    version="0.0.1",
    packages=find_packages(include=[], exclude=[]),
    include_package_data=True,
    install_requires=[
        "flask",
    ],
    cmdclass={
        "vet": VetCommand,
        "fmt": FmtCommand,
        "server": ServerCommand,
    },
)
