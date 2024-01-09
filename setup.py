from setuptools import setup, find_packages


requires = [
    'pygame',
    
]


setup(
    name='A* Algorithm',
    version='1',
    description='A* Algorithm',
    classifiers=[
        'Programming Language :: Python',
    ],
    author='Tom Hildebrand',
    author_email='thomas.hildebrand1@gmail.com',
    url='',
    keywords='python pygame A*',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,

)
