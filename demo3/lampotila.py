import Adafruit_DHT

# Anturin määritykset
SENSOR = Adafruit_DHT.DHT11
SENSOR_PIN = 5

def get_temp():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
        print('Ilmankosteus: {}, lämpötila: {}'.format(humidity, temperature))
        return (temperature, humidity) 
    except Exception as e:
        print("Virhe:", str(e))
        return -1

if __name__ == "__main__":
    get_temp()