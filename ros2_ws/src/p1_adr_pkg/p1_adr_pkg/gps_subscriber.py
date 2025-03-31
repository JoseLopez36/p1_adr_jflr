import rclpy
from rclpy.node import Node

# Import NavSatFix message
from sensor_msgs.msg import NavSatFix

# GpsSubscriber class
class GpsSubscriber(Node):

    def __init__(self):
        super().__init__('gps_subscriber')
        
        # Create subscription to GPS data
        self.subscription = self.create_subscription(
            NavSatFix,
            'gps_data',
            self.gps_callback,
            10)
        
        self.get_logger().info('GPS Subscriber initialized')

    def gps_callback(self, msg):
        # Process the received GPS data
        self.get_logger().info(
            f'Received GPS: Lat={msg.latitude:.6f}, Long={msg.longitude:.6f}, Alt={msg.altitude:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = GpsSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()
    return 0

if __name__ == '__main__':
    main()