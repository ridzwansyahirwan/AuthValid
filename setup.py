from setuptools import setup, find_packages

setup(
    name='TokenForge',
    version='0.1',
    packages=find_packages(),
    description='A package for JWT token management and authentication',
    author='Mohammad Ridzwan Syah bin Irwan',
    author_email='ridzwansyahirwan@gmail.com',
    url='',
    install_requires=[
        'Flask',
        'python-dotenv',
        'PyJWT',
    ],
)