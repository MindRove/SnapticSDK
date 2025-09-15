
from snaptic_sdk import PySnapticSDK

def initialize_snaptic():
    """Initialize the Snaptic SDK and return the instance."""
    try:
        snaptic = PySnapticSDK()
        print("BLE state:", snaptic.get_ble_state())
        return snaptic
    except Exception as e:
        print("Failed to initialize Snaptic SDK:", e)
        exit()

def main():
    """Main function to test the Snaptic SDK."""
    # Initialize the Snaptic SDK    
    snaptic = initialize_snaptic()

    # Search for Bluetooth devices
    print("Searching for devices...")
    devices = snaptic.search_devices()

    # Connect to the first device found
    if devices:
        print("Device(s) found:")    
        for device in devices:
            print(f"  Name: {device.Name}, Id: {device.Id}")

        device = devices[0]
        print("Connecting to device:", device.Name + ", Id: " + device.Id)
        connected = snaptic.connect_device(device)

        if connected:
            print("Connected  successfully.")   
            print("BLE state:", snaptic.get_ble_state())

            # Wait and retrieve IMU data
            last_spo2 = None
            for _ in range(3):
                data = snaptic.get_imu_data()
                if data:
                    print(f"IMU data received at {data['time']}ms:")
                    for pkt in data["packets"]:
                        print(f"  PacketNum: {pkt['PacketNum']}, PacketTime: {pkt['PacketTime']}")
                        print(f"    MainAccel: X={pkt['MainAccel']['X']}, Y={pkt['MainAccel']['Y']}, Z={pkt['MainAccel']['Z']}" )
                        print(f"    SubAccel: X={pkt['SubAccel']['X']}, Y={pkt['SubAccel']['Y']}, Z={pkt['SubAccel']['Z']}" )
                        print(f"    MainGyro: X={pkt['MainGyro']['X']}, Y={pkt['MainGyro']['Y']}, Z={pkt['MainGyro']['Z']}" )
                        print(f"    SubGyro: X={pkt['SubGyro']['X']}, Y={pkt['SubGyro']['Y']}, Z={pkt['SubGyro']['Z']}" )
                else:
                    print("No IMU data received within timeout.")
            
            # Wait and retrieve SpO2 data
            for _ in range(3):
                spo2 = snaptic.get_spo2_data()
                if spo2 and spo2 != last_spo2:
                    print(f"SpO2 data received")
                    print(f"  Led: {spo2['led']}")
                    last_spo2 = spo2

                else:
                    print("No SpO2 data received within timeout.")

            # Disconnect from the device
            print("Disconnecting from device...")
            snaptic.disconnect_device()
        else:
            print("Failed to connect to device:", device.Name)
            return
    else:
        print("No devices found. Exiting...")



if __name__ == "__main__":
    print("Starting Snaptic SDK test...")
    main()