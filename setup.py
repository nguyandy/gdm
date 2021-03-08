from distutils.core import setup, Extension
import distutils.command.bdist_conda

setup(
    name="gdm",
    version="1.0",
    distclass=distutils.command.bdist_conda.CondaDistribution,
    conda_buildnum=1,
)