from setuptools import find_packages, setup

package_name = 'p1_adr_pkg'

setup(
    name=package_name,
    version='1.0.0',
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
    description='Paquete para la práctica 1 de Ampliación de Robótica',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_publisher = p1_adr_pkg.gps_publisher:main',
            'gps_subscriber = p1_adr_pkg.gps_subscriber:main'
        ],
    },
)
