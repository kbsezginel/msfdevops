import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name='msfdevops',
        version='0.1.0',
        description='MolSSI Bootcamp 2018 Devops',
        author='Kutay B. Sezginel',
        author_email='kbs37@pitt.edu',
        url="https://github.com/kbsezginel/msfdevops",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[
        ],
        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=False,
    )
