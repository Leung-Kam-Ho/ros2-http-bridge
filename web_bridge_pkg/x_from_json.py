from geometry_msgs.msg import Twist


def twist_from_json(json_data : dict) -> Twist:
    twist = Twist()
    twist.linear.x = json_data.get('linear', {}).get('x', 0.0)
    twist.linear.y = json_data.get('linear', {}).get('y', 0.0)
    twist.linear.z = json_data.get('linear', {}).get('z', 0.0)
    twist.angular.x = json_data.get('angular', {}).get('x', 0.0)
    twist.angular.y = json_data.get('angular', {}).get('y', 0.0)
    twist.angular.z = json_data.get('angular', {}).get('z', 0.0)
    return twist