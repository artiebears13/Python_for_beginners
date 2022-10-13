from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(name='my_incredible_lib',
      version='0.1.0',
      description='Hometask 3',
      long_description=long_description,
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      entry_points={
          "console_scripts": [
              "dzeta=dzeta:main",
              "lorenz=main",
          ]
      },
      long_description_content_type="text/markdown",
      author='Artem',
      install_requires=REQUIREMENTS,
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6')