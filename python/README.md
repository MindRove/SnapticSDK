# Snaptic Python SDK

## Overview

The Snaptic Python SDK is a wrapper around the Snaptic .NET SDK, providing an easy-to-use interface for interacting with Snaptic devices. This SDK enables searching for BLE devices, connecting and disconnecting from device, and retrieving both IMU sensors and SpO2 sensor data from connected device.

## Features

- Search for available Snaptic BLE devices
- Connect and disconnect from device
- Retrieve real-time IMU sensors data (accelerometer, gyroscope)
- Retrieve real-time SpO2 sensor data
- Manage BLE state tracking

## Requirements

- Python 3.x
- .NET Core runtime (for `pythonnet` integration)
- Snaptic SDK Wheel (.whl) package (provided)
- Bluetooth-enabled hardware

## Installation

To use the Snaptic Python SDK, ensure you have the required dependencies installed:

```sh
pip install pythonnet
```
Run the following command to install the Snaptic SDK from the provided .whl file:

```sh
pip install snaptic_sdk-x.x.x-py3-none-any.whl
```

## Usage
### Initializing the SDK
```python
from snaptic_sdk import PySnapticSDK

snaptic = PySnapticSDK()
```
### Searching for Devices
```python
devices = snaptic.search_devices()
print("Devices found:")
for device in devices:
    print(f"  Name: {device.Name}, Id: {device.Id}")
```
### Connecting to a Device
```python
if devices:
    device = devices[0]
    connected = snaptic.connect_device(device)
    if connected:
        print("Connected to:", device.Name)
```
### Retrieving IMU Data
```python
data = snaptic.get_imu_data()
if data:
    print(f"IMU data received at {data['time']}ms:")
    for pkt in data["packets"]:
        print(f"  PacketNum: {pkt['PacketNum']}, PacketTime: {pkt['PacketTime']}")
        print(f"    MainAccel: X={pkt['MainAccel']['X']}, Y={pkt['MainAccel']['Y']}, Z={pkt['MainAccel']['Z']}")
        print(f"    SubAccel: X={pkt['SubAccel']['X']}, Y={pkt['SubAccel']['Y']}, Z={pkt['SubAccel']['Z']}")
        print(f"    MainGyro: X={pkt['MainGyro']['X']}, Y={pkt['MainGyro']['Y']}, Z={pkt['MainGyro']['Z']}")
        print(f"    SubGyro: X={pkt['SubGyro']['X']}, Y={pkt['SubGyro']['Y']}, Z={pkt['SubGyro']['Z']}")
```
### Retrieving SpO2 Data
```python
spo2 = snaptic.get_spo2_data()
if spo2:
    print(f"SpO2 data received")
    print(f"  Led: {spo2['led']}")
```
### Disconnecting from a Device
```python
snaptic.disconnect_device()
print("Disconnected from device.")
```
### Running the Example Test Script
A test script is provided in snaptic_test.py. To execute it:

```sh
python snaptic_test.py
```
This script will:

1. Search for available Snaptic BLE devices
2. Connect to the first detected device
3. Retrieve and print IMU and SpO2 sensor data for a few iterations
4. Disconnect from the device

## Contact
For further support and inquiries, please contact the Snaptic development team **[info@mindrove.com]**.
