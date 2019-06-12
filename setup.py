import setuptools

setup = dict(
    name="Multi Purpose Arduino Controller",
    version="0.<",
    author="Julian Kimmig",
    author_email="julian-kimmig@gmxREADME.md.net",
    description="Controll Arduino modules",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["multi_purpose_arduino_controller"],
    url="https://github.com/JulianKimmig/json_dict",
    # packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
if __name__ == "__main__":
    setuptools.setup(**setup)
