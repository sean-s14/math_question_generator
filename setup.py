import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="math-question-generator",
    version="1.0.1",
    description="Generate math questions & answers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shaun-ps-04/math_question_generator",
    author="Shaun Stocker",
    author_email="s.stocker04@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["maths_question_generator"],
    include_package_data=True,
    # install_requires=["feedparser", "html2text"],
    # entry_points={
    #     "console_scripts": [
    #         "realpython=reader.__main__:main",
    #     ]
    # },
)
