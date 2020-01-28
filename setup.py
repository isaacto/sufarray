import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sufarray_kkto',
    version='0.0.1',
    python_requires='~=3.5',
    author='Isaac To',
    author_email='isaac.to@gmail.com',
    description='Suffix Array for all-substring search',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/isaacto/sufarray',
    packages=setuptools.find_packages(),
    package_data={'sufarray': ['py.typed']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
