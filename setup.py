from setuptools import setup, find_packages

setup(
    name='lx-vsm-py',
    version='1.0',
    packages=['lx_vsm_py'],
    install_requires=[
        'requests',
        'cyclonedx-bom'
    ],
    entry_points={
        'console_scripts': [
            'lx-vsm-py = lx_vsm_py.lx_vsm_py:main'
        ]
    }
)
