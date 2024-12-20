# Team-UChecked
OpenSource Software Design ( Team Project )


# IoT Attendance Tracking Solution Using oneM2M

## Problem Statement

Tracking student attendance is an essential task in schools and universities, but it often relies on manual methods or isolated management systems. These approaches are inefficient and prone to errors, such as data omissions or incorrect entries.

Our project leverages IoT technology and the **oneM2M standard** to develop an **efficient and reliable attendance tracking system**. This solution allows administrators to monitor attendance in real-time while securely storing and managing the data.

## Proposed Solution

Our solution utilizes the **oneM2M Mobius platform** to deliver the following features:

- **Automated Data Recording**: A virtual beacon is used to input student IDs, which are automatically stored in the Mobius server.
- **Real-Time Data Access**: Retrieve the latest attendance data from the Mobius server in real-time.
- **Scalability**: Extendable to support sensors and actuators for various IoT-based attendance scenarios.

This system enhances efficiency and contributes to improving the learning environment.

## Features and Functionalities
### 1. **Sensor Data Collection**
- Sends simulated temperature and presence data to the Mobius server.
- Stores sensor data in a `SensorAE` container on the server.  
  
### 2. **Actuator Control**
- Analyzes the latest sensor data and sends control commands, such as turning on/off heating systems, based on predefined conditions.
- Uses the `ControlAE` container to send commands to actuators.  

### 3. **Data Monitoring**
- Retrieves the latest attendance records and sensor data in real-time from the Mobius server.  

## oneM2M Features Used

This project leverages the following key features of the **oneM2M standard**:

1. **Container**:
   - A container (`attendance`) is created to store attendance data.
   - Facilitates hierarchical data management and organization.
   - Containers (`attendance`, `SensorAE`, `ControlAE`) are created to organize data hierarchically.
   - Used for efficient data management and retrieval.  

2. **ContentInstance**:
   - Each student's attendance record is stored as a `ContentInstance`.
   - The `latest` resource is used to efficiently retrieve the most recent attendance data.

3. **Mobius Platform**:
   - Mobius, as an IoT platform compliant with the oneM2M standard, manages data storage, retrieval, and efficient data flows.

These features enable seamless storage, management, and retrieval of attendance records.

## Devices and Software Used

### 1. Mobius Server
- **Platform**: Mobius (based on the oneM2M standard)
- **Role**: Stores and manages attendance data.

### 2. Python Scripts
- Client-side application to send and manage attendance data on the server.
- Key files:
  - `main.py`: Main execution script.
  - `mobius.py`: Handles communication with the Mobius server.
  - `sensor_data.py`: Sends sensor data (temperature and presence) to the Mobius server and stores it in a database.
   - `control_data.py`: Analyzes sensor data and sends commands (e.g., turn on/off heating) to the Mobius server.
   - `actuator_control.py`: Retrieves commands from the Mobius server and executes actions accordingly.


### 3. Virtual Beacon
- Simulates student ID input and transmits it to the Mobius server.

### 4. Other Tools
- **`requests` Library**: Used for handling HTTP requests.
- **Mobius Server Hosting**: Hosted locally or in the cloud.

## Project Architecture

### Resource Tree
Mobius (CSEBase)   
└── attendance (Container)   
├── latest (Link to the latest contentInstance)   
└── {resourceName} (ContentInstance: Each attendance record)   
├── SensorAE (Container)  
│   ├── temperature (ContentInstance)  
│   └── presence (ContentInstance)  
├── ControlAE (Container)  
│   └── commands (ContentInstance)  
└── ActuatorAE (Container)  
    └── actions (ContentInstance)

### Data Flow
1. Python script sends student ID data to the Mobius server (`POST` request).
2. Mobius stores the data as a `ContentInstance`.
3. Users retrieve the latest data using a `GET /latest` request.
4. The control script analyzes the sensor data and sends commands to the Mobius server.
5. Actuator script retrieves commands and performs the corresponding actions.


## How to Execute

### 1. Start the Mobius Server
- Run the Mobius server locally or on the cloud.

### 2. Set Up the Python Client
- Download the project code and install the required dependencies:
  ```bash
  pip install requests

### 3. Run the System
- Execute the main.py script to send and retrieve attendance data:
  ```bash
  python main.py

### Execute the sensor data script to send sensor data to the Mobius server:
  
  ```bash
  python sensor_data.py
```
### Execute the control data script to analyze data and send commands:
   
   ```bash
   python control_data.py
```
### Execute the actuator control script to retrieve commands and perform actions:

   ```bash
   python actuator_control.py
```

# Smart Campus Web Application

---

## Features
- **User Authentication**: Simple username-password-based login.
- **Session Management**: Tracks user login state across pages.
- **Routes**: Multiple routes for different pages (e.g., `login`, `mainpage`, `daeyangai`).
- **Templating**: Dynamic HTML rendering using Jinja templates.

---

## Prerequisites

Ensure the following are installed on your system:
- **Python 3.x**
- **Flask** (`pip install flask`)

---

# YOLOv5 Space Congestion Analysis

## Overview
This project utilizes the YOLOv5 object detection model to analyze space congestion using a webcam feed. The application detects people and specific objects (laptops, cups, books, bags, handbags) in predefined regions of interest (ROIs) on the video stream. The results are displayed on the screen in real-time, providing the number of people and the presence of target objects in each ROI.

## Features
- Real-time object detection using YOLOv5.
- Tracks the number of people in multiple regions of interest.
- Detects specific objects including:
  - Laptop
  - Cup
  - Book
  - Bag
  - Handbag
- Highlights detected objects and displays relevant information directly on the video feed.

## Requirements
Make sure you have the following installed before running the program:
- Python 3.7 or higher
- OpenCV
- PyTorch
- YOLOv5 (loaded via `torch.hub`)

Install the necessary dependencies with:
```python
pip install opencv-python-headless torch torchvision
```
## How to Run
1. Clone the repository or download the script.
2. Open a terminal in the directory containing the script.
3. Run the script:
```python
pip install opencv-python-headless torch torchvision
```
## How to Run
1. Clone the repository or download the script.
2. Open a terminal in the directory containing the script.
3. Run the script:
```python
python your_script_name.py
```
4. The webcam feed will open, displaying the analysis of the predefined ROIs.

### Controls
- Press `q` to exit the application.

## Code Explanation
### Regions of Interest (ROIs)
The application defines four rectangular areas on the video feed where it performs object detection. These areas are represented as coordinates:
```python
rectangles = [(100, 100, 800, 500), (900, 100, 1600, 500), (100, 600, 800, 1000), (900, 600, 1600, 1000)]
```
### Object Detection
The YOLOv5 model detects objects in each ROI. Specific objects and people are tracked:
- **Class 0**: Person
- **Class 63**: Laptop
- **Class 41**: Cup
- **Class 73**: Book
- **Class 24**: Bag
- **Class 26**: Handbag

### Visual Feedback
- **Red Rectangles**: Indicate the ROIs.
- **Green Bounding Boxes**: Highlight detected objects within each ROI.
- Text information on the screen:
  - Number of people in each area.
  - Whether specific objects are present in each area.

## Example Use Case
This application can be used to monitor congestion in areas such as:
- Libraries
- Cafeterias
- Public spaces
- Workspaces

It provides real-time insights into the number of people and the presence of specific objects, aiding in better space utilization and management.

## Acknowledgments
- **YOLOv5 Model**: Powered by [Ultralytics](https://github.com/ultralytics/yolov5).
- **OpenCV**: For real-time video processing.
- **PyTorch**: For deep learning model support.

## Notes
- Make sure your webcam is connected and functioning.
- Adjust the ROI coordinates (`rectangles`) in the code as per your webcam feed resolution and requirements.

## License
This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.

