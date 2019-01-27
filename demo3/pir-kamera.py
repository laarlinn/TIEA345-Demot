import RPi.GPIO as GPIO
from time import sleep
import subprocess
GPIO.setmode(GPIO.BCM)

# PIR-anturin pinni
PIR_PIN = 4

# Kuvien ottamisen aikaväli
SLEEP_TIME = 5
GPIO.setup(PIR_PIN, GPIO.IN)

def main():
    try:
        print("Odotetaan liiketunnistinta..")
        while True:
            if GPIO.input(PIR_PIN) == 1:
                print("Liikettä havaittu, tallennetaan..")
                save_picture()
                print("Nukutaan {} s.".format(SLEEP_TIME))
                sleep(SLEEP_TIME)
                print("Odotetaan liiketunnistinta..")
            else: sleep(0.5)
            

    except KeyboardInterrupt as e:
        print("Lopetetaan..")

def save_picture():
    try: # helpompaa kuin python-kirjastojen käyttö
        subprocess.call(["raspistill", "-o", "/home/pi/motion.jpg"])
        print("Kuva tallennettu! (periaatteessa)")
    except Exception as e:
        print("Kuvan tallennus epäonnistui: " + str(e))

if __name__ == "__main__":
    main()