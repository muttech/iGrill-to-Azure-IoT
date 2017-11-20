# iGrill-to-Azure-IoT
Push iGrill2 data to Azure IoT Hub

Initial code for interacting with iGrill2 found at [iGrill_bbqmqtt](https://github.com/bjoernhoefer/iGrill_bbqmqtt)

### Requires
* [bluepy](https://github.com/IanHarvey/bluepy)
* requests - pip install requests

## Usage
### iGrill
1. Enable Bluetooth - sudo hciconfig hci0 up
2. Start the iGrill app and connect it to your iGrill2. 
3. Set an alarm for any of the connected probes.
4. Disconnect the iGrill app and run app.py