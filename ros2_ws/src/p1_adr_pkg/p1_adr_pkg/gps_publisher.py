import rclpy
from rclpy.node import Node
import numpy as np
from dataclasses import dataclass

# Import NavSatFix message
from sensor_msgs.msg import NavSatFix

@dataclass
class GpsData:
    lat: float
    long: float
    alt: float

# GpsPublisher class
class GpsPublisher(Node):

    def __init__(self):
        super().__init__('gps_publisher')
        # Create publisher for GPS data (NavSatFix)
        self.gps_publisher_ = self.create_publisher(NavSatFix, 'gps_data', 10)

        # Create update timer each 10 ms
        self.timer = self.create_timer(0.01, self.update)
        
        # Base GPS coordinates (example: Cádiz)
        self.base_lat = 36.53
        self.base_long = -6.29
        self.base_alt = 10.0
        
        # Noise parameters
        self.hor_noise_std = 2.0     # Standard deviation for lat/long noise
        self.ver_noise_std = 10.0    # Standard deviation for altitude noise
        
        self.get_logger().info('GPS Publisher initialized')

    def update(self):
        # Generate synthetic data
        gps_data = self.generate_gps_data()

        # Create GPS message
        gps_msg = self.create_gps_msg(gps_data.lat, gps_data.long, gps_data.alt)

        # Publish message
        self.publish_gps(gps_msg)
        
    def generate_gps_data(self):
        # Generate data with Additive-White-Gaussian-Noise (AWGN)
        lat = self.base_lat + np.random.normal(0, self.hor_noise_std)
        long = self.base_long + np.random.normal(0, self.hor_noise_std)
        alt = self.base_alt + np.random.normal(0, self.ver_noise_std)
        
        return GpsData(lat=lat, long=long, alt=alt)

    def create_gps_msg(self, lat, long, alt):
        # Create synthetic GPS data as NavSatFix message
        gps_msg = NavSatFix()
        gps_msg.header.stamp = self.get_clock().now().to_msg()
        gps_msg.header.frame_id = 'map'
        gps_msg.latitude = lat
        gps_msg.longitude = long
        gps_msg.altitude = alt
        return gps_msg

    def publish_gps(self, gps_msg):
        self.gps_publisher_.publish(gps_msg)

def main(args=None):
    rclpy.init(args=args)
    node = GpsPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()
    return 0

if __name__ == '__main__':
    main()