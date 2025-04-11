from flask import Flask, request, jsonify
import rclpy
from geometry_msgs.msg import Twist
from web_bridge_pkg.x_from_json import twist_from_json
import threading 
from rclpy.node import Node


class WebBridgeNode(Node):
    def __init__(self):
        super().__init__('web_bridge_node')

        # Initialize Flask app
        self.app = Flask(__name__)
        self.setup_routes()
        # Initialize ROS2 publisher
        self.publisher_cmd_vel = self.create_publisher(Twist, 'cmd_vel', 10)

        # Start Flask server in a separate thread
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.daemon = True
        self.server_thread.start()

    def setup_routes(self):
        self.app.add_url_rule('/cmd_vel', 'cmd_vel', self.handle_cmd_vel, methods=['POST'])

    def handle_cmd_vel(self):
        """
        Example curl command to test this endpoint:
        curl -X POST http://localhost:8888/cmd_vel -H "Content-Type: application/json" -d '{"linear": {"x": 0.5, "y": 0.0, "z": 0.0}, "angular": {"x": 0.0, "y": 0.0, "z": 0.5}}'
        """
        json_data = request.get_json()
        print(f"Received JSON data: {json_data}")
        twist = twist_from_json(json_data)
        self.publisher_cmd_vel.publish(twist)
        return jsonify({'message': 'Data received successfully'}), 200

    def run_server(self):
        self.app.run(host='0.0.0.0', port=8888)


def main(args=None):
    rclpy.init(args=args)
    web_bridge_node = WebBridgeNode()
    rclpy.spin(web_bridge_node)
    web_bridge_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()