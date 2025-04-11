# ROS 2 HTTP Web Bridge

This is a simple template for bridging HTTP API requests to ROS 2 topics using Flask. It allows external clients (e.g., a web frontend or mobile app) to send JSON-formatted commands via HTTP POST, which are then converted into ROS 2 messages and published into the ROS network.

## Features

- Python-only
- HTTP API via Flask
- Publishes geometry messages (e.g. `Twist` to `cmd_vel`)
- Easily extensible to support more topics or message types

## Example Use Case

Send velocity commands from a web interface, mobile app, or any HTTP client to control a robot using the `/cmd_vel` topic.

## Prerequisites

- ROS 2 (e.g., Humble, Foxy)
- `geometry_msgs`
- `Flask` Python package:
  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/universal_ws.git
   cd universal_ws/src/web_bridge_pkg
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the Package:**
   ```bash
   cd ../../..
   colcon build --packages-select web_bridge_pkg
   ```

4. **Source the Workspace:**
   ```bash
   source install/setup.bash
   ```

## Usage

1. **Run the Node:**
   ```bash
   ros2 run web_bridge_pkg web_bridge_node
   ```

2. **Send a Command:**
   Use `curl` or any HTTP client to send a POST request:
   ```bash
   curl -X POST http://localhost:8888/cmd_vel -H "Content-Type: application/json" -d '{"linear": {"x": 0.5, "y": 0.0, "z": 0.0}, "angular": {"x": 0.0, "y": 0.0, "z": 0.5}}'
   ```

## Configuration

- **Port:** The Flask server runs on port `8888`. You can change this in the `web_bridge_node.py` file.
- **Topics:** The node currently publishes to the `/cmd_vel` topic. You can modify this in the `WebBridgeNode` class.
