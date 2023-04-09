from setuptools import find_packages, setup
from pathlib import Path

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cache_storage",
    # packages=find_packages(include=["yahoo_api"], exclude=("tests",)),
    keywords="yahoo financials cache storage dropbox",
    packages=["cache_storage", "cache_storage.src"],
    version="0.0.1",
    description="Cache Storage",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MihaiBlebea/cache_storage_python",
    author="Mihai Blebea",
    author_email="mihaiserban.blebea@gmail.com",
    license="MIT",
    install_requires=["dropbox"],
    setup_requires=["dropbox"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
