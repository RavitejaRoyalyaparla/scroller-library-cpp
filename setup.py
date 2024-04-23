from setuptools import setup, find_packages

setup(
    name='scroller',
    version='0.1',
    packages=find_packages(),
    description='A simple scroller feed library for Django projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ravi Teja',
    author_email='ravitejaroy@gmail.com',
    url='https://github.com/yourusername/scroller-feed',
    license='MIT',
    install_requires=[
        'Django>=3.2'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
