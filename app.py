import bluepy.btle as btle
import binascii
from azureiot import azureiot

MESSAGE_FORMAT = "{'Probe':%s,'Temp':%s}"

# Update this to the Bluetooth Mac Address of your iGrill - can be found via: sudo hcitool lescan
address =  "70:91:8a:14:bc:5f"
printoutloud = True

# Replace <IotHubName> with your Azure IoT Hub Service Name.  Replace <SharedAcessKey> with your key.
connectionString = 'HostName=<IotHubName>.azure-devices.net;SharedAccessKey=<SharedAccessKey>'
iotclient = azureiot(connectionString)
# Replace with the DeviceId configured in Azure IoT Hub
deviceId = '<deviceId>'
    
class grillDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        formatedData = binascii.b2a_hex(data)
        probes = {52 : '1',
                57 : '2',
                62 : '3',
                67 : '4'
        }
        if cHandle in (52,57,62,67):
            temperature = int(formatedData[0:len(formatedData)-4],16)
            iotclient.sendMessage(deviceId, MESSAGE_FORMAT % (probes[cHandle],temperature) )
            if printoutloud:
                print "Probe ", probes[cHandle], ": ", temperature
        elif cHandle == 82:
            batteryvalue = int(formatedData,16)
            if printoutloud:
                print "Battery: ", batteryvalue
        else:
            if printoutloud:
                print "Unknown cHandle: ", cHandle, " - Value: ", formatedData

igrill = btle.Peripheral(address)
igrill.setDelegate(grillDelegate())

while True:
    if igrill.waitForNotifications(60):
        continue