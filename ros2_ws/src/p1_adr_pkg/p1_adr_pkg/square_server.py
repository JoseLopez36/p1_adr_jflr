import rclpy
from rclpy.node import Node
from p1_adr_interfaces.srv import Square

class SquareServer(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(
            Square, 
            'square', 
            self.calculate_square_callback)
        self.get_logger().info('Square service server has been started')
        
    def calculate_square_callback(self, request, response):
        # Calculate the square of the input number
        response.x_squared = request.x * request.x
        self.get_logger().info(
            f'Request: {request.x:.2f} -> Response: {response.x_squared:.2f}')
        return response

def main(args=None):
    rclpy.init(args=args)
    square_server = SquareServer()
    try:
        rclpy.spin(square_server)
    except KeyboardInterrupt:
        pass
    finally:
        square_server.destroy_node()
        rclpy.shutdown()
    return 0

if __name__ == '__main__':
    main()