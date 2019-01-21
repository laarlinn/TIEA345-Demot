import Adafruit_DHT

# Anturin määritykset
SENSOR = Adafruit_DHT.DHT11
SENSOR_PIN = 5

def main():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
        print('Ilmankosteus: {}, lämpötila: {}'.format(humidity, temperature))
    except KeyboardInterrupt:
        print("Closing..")
    except Exception as e:
        print("Virhe:", str(e))

if __name__ == "__main__":
    main()