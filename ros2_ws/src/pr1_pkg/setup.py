from setuptools import find_packages, setup

package_name = 'pr1_pkg'

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
    maintainer='Jose Francisco López Ruiz',
    maintainer_email='josloprui6@alum.us.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_publisher = pr1_pkg.gps_publisher:main',
            'gps_subscriber = pr1_pkg.gps_subscriber:main'
        ],
    },
)
