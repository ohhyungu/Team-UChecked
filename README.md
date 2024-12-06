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
