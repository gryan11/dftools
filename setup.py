from setuptools import setup

setup(name='df-tools',
        version='1.0.0',
        packages=['dftools'],
        entry_points={
            'console_scripts': [
                'showdf = dftools.show_df:main',
                'statdf = dftools.stat_df:main',
                'cmpdf = dftools.cmp_df:main',
                'latexdf = dftools.latex_df:main',
                ]
            },
        install_requires=[
            'pandas',
            ]
        )
