from setuptools import find_packages, setup

package_name = 'turtlesim_draw'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ketki',
    maintainer_email='ketki@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'ivdc1= turtlesim_draw.IVDC1:main',
        'ivdc2=turtlesim_draw.IVDC2:main',
        'my_script=turtlesim_draw.my_script1:main',

        ],
    },
)
