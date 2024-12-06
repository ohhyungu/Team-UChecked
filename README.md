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

## oneM2M Features Used

This project leverages the following key features of the **oneM2M standard**:

1. **Container**:
   - A container (`attendance`) is created to store attendance data.
   - Facilitates hierarchical data management and organization.

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
### Data Flow
1. Python script sends student ID data to the Mobius server (`POST` request).
2. Mobius stores the data as a `ContentInstance`.
3. Users retrieve the latest data using a `GET /latest` request.

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
