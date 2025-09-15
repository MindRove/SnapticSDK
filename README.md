# Snaptic SDK for Windows

## Overview

The **Snaptic SDK** provides a Bluetooth Low Energy (BLE) interface to connect, stream, and manage data from Snaptic IMU sensor devices. This document outlines integration and usage for **Windows** applications.

---

## Supported Platform

- Windows 10 or higher 
- .NET 8 MAUI or WinAppSDK

---

## Installation

1. Add the file `SnapticSDK.dll` from `Platforms/Windows` into your project.
2. In your `.csproj` file, make sure:

```xml
<ItemGroup>
  <Reference Include="SnapticSDK">
    <HintPath>Platforms\Windows\SnapticSDK.dll</HintPath>
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </Reference>
</ItemGroup>
```

## Initialization

```csharp
using Snaptic_SDK;

var sdk = new SnapticSDK();
```

## Device Discovery

```csharp
var devices = await sdk.SearchDevices();
foreach (var device in devices)
{
    Console.WriteLine($"Found: {device.Name}");
}
```

## Connecting to a Device
```csharp
if (devices != null && devices.Count > 0)
{
    var device = devices.First();
    bool isConnected = await sdk.ConnectToDevice(device);
    Console.WriteLine(isConnected ? "Connected Successfully" : "Connection Failed");
}
```

## Disconnecting from a Device
```csharp
sdk.DisconnectDevice();
```

## Receiving IMU Data
Subscribe to the IMU data event:
```csharp
sdk.OnIMUDataReceived += (IMUDataPacket data) =>
{
    Console.WriteLine($"Time: {data.time}");
    Console.WriteLine($"IMU Packet #{data.packetNumber}");
    foreach (var packet in data.packets)
    {
        Console.WriteLine($"Main Accel: X={packet.MainAccel.X}, Y={packet.MainAccel.Y}, Z={packet.MainAccel.Z}");
        Console.WriteLine($"Sub Accel: X={packet.SubAccel.X}, Y={packet.SubAccel.Y}, Z={packet.SubAccel.Z}");
        Console.WriteLine($"Main Gyro: X={packet.MainGyro.X}, Y={packet.MainGyro.Y}, Z={packet.MainGyro.Z}");
        Console.WriteLine($"Sub Gyro: X={packet.SubGyro.X}, Y={packet.SubGyro.Y}, Z={packet.SubGyro.Z}");
    }
};
```
## Receiving raw SpO2 Data
Subscribe to the SpO2 data event:
```csharp
sdk.OnSpO2DataReceived += (SpO2DataPacket data) =>
{
    Console.WriteLine($"SpO2 Packet #{data.PacketNum}");
    for (int i = 0; i < data.LED.Count; i++)
    {
        Console.WriteLine($"LED[{i}] = {data.LED[i]}");
    }
};
```

## BLE State Management
The SDK manages BLE states internally but provides an API to check the current state:
```csharp
BLEState currentState = sdk.CurrentState;
Console.WriteLine($"Current BLE State: {currentState}");
```

## Troubleshooting
- **Device not found**: Ensure Bluetooth is enabled and the device is in pairing mode.
- **Connection failed**: Verify that the device is not connected elsewhere.
- **Data not received**: Ensure IMU notifications are enabled after connecting.


## Contact

For feature requests or bugs, contact **[info@mindrove.com]**