from setuptools import setup, find_packages

setup(
    name="vaqm",
    version="0.0.1",
    description="UGE qsub command wrapper",
    author="riku.okajima",
    author_email="riku.okajima@gmail.com",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={"console_scripts": ["vaqm = vaqm.vaqm:main"]}
)