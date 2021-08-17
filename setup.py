"""Setup for dinner at clementi package."""

from setuptools import setup,find_packages

__pkg_name__ = 'dinner_at_clemz'


with open('README.md') as f:
    README = f.read()

setup(
    author="meja_bundar_dover_crescent",
    maintainer_email="dinner_at_clementi@clementi_mail.com",
    name=__pkg_name__,
    license="MIT",
    description='dinner_at_clementi is a python package that is essential for launching the next scalable unicorn in South East Asia.',
    version='v0.0.1',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/chrishendra93/xpore',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
            ],
    python_requires=">=3.5",
    entry_points={'console_scripts': ["clementi-{}.src.main:main".format(__pkg_name__)]},
    classifiers=[
        'Development Status :: None',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Dinner at Clementi',
    ],
)