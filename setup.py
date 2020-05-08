from setuptools import setup

setup(name='df-tools',
        version='1.0.0',
        # packages=['tools'],
        entry_points={
            'console_scripts': [
                'showdf = showdf:main',
                'cmpdf = cmp_df:main',
                'latexdf = latex_df:main',
                ]
            },
        )
