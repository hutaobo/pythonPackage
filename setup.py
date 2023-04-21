# _*_ coding : utf-8 _*_
# @Time : 2023-04-21 13:38
# @Author : Taobo Hu
# @File : setup
# @Project : pythonPackage

from setuptools import setup

setup(
    name='pythonPackage',
    version='0.0.1',
    description='My private package form private github repo',
    url='git@github.com:hutaobo/pythonPackage-sdk-package.git',
    author='Taobo Hu',
    author_email='taobo.hu@scilife.se',
    license='unlicense',
    packages=['pythonPackage'],
    zip_safe=False
)
