from setuptools import setup

setup(name='df-tools',
        version='1.0.0',
        # packages=['tools'],
        entry_points={
            'console_scripts': [
                'showdf = show_df:main',
                'statdf = stat_df:main',
                'cmpdf = cmp_df:main',
                'latexdf = latex_df:main',
                ]
            },
        )
