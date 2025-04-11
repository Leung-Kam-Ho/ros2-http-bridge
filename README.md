# ROS 2 HTTP Web Bridge (Flask-Based)

This is a simple template for bridging HTTP API requests to ROS 2 topics using Flask. It allows external clients (e.g., a web frontend or mobile app) to send JSON-formatted commands via HTTP POST, which are then converted into ROS 2 messages and published into the ROS network.

## Features

- Python-only, no JavaScript frontend
- HTTP API via Flask (no WebSockets)
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
