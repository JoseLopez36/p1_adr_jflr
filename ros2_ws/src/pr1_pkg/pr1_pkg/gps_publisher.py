import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

# GpsPublisher class
class GpsPublisher(Node):

    def __init__(self):
        # Create publisher for GPS data (NavSatFix)
        gps_publisher_ = node.create_publisher(NavSatFix, 'gps_data', 10)

        # Create update timer each 10 ms


    def shutdown(self):

    
    def update(self):
        # Generate synthetic data
        gps_data = self.generate_gps_data()

        # Create GPS message
        gps_msg = self.create_gps_msg(gps_data.lat, gps_data.long, gps_data.alt)

        # Publish message
        self.publish_gps(gps_msg)

        # Log message published
        
    def generate_gps_data(self):
        # Generate data with Additive-White-Gaussian-Noise (AWGN)
        lat = 
        long = 
        alt =

    def create_gps_msg(self, lat, long, alt):
            # Crear datos GPS sintéticos como mensaje de tipo NavSatFix
            gps_msg = NavSatFix()
            gps_msg.header.stamp = rclpy.clock.Clock().now().to_msg()
            gps_msg.header.frame_id = 'map'
            gps_msg.latitude = lat
            gps_msg.longitude = long
            gps_msg.altitude = alt
            return gps_msg

    def publish_gps(self, gps_msg):
        gps_publisher_.publish(gps_msg)

if __name__ == '__main__':
    node = GpsPublisher()
    rclpy.spin(node)
    node.shutdown()
    rclpy.shutdown()

# Entregar como repo público p1_adr_jflr, en un correo el enlace del repo