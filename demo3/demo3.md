# Demo 3: Lämpötila-anturi ja kamera
## 3.1
Ajamalla `python3 lampotila.py` näyttöön tulostuu:

```
pi@raspberrypi:~/demo3 $ python3 lampotila.py
Ilmankosteus: 21.0, lämpötila: 19.0
```
## 3.2
Loin Googlen Developer Consolessa uuden projektin `tiea345`, enabloin Google Sheets API:n, ja loin uuden Service Accountin. Latasin JSON-tiedoston ja siirsin sen raspille.

client_email:
```
"client_email": "tiea345@tiea345-229916.iam.gserviceaccount.com",
```

Taulukko jaettu.

## 3.3
Kuva: https://drive.google.com/open?id=1Y-KS--hmIgppUxRHotX5BHsbFQZgmwBC

Otin kuvan komennolla
```
raspistill -o testi1.jpg
```
Video: https://www.youtube.com/watch?v=A-g7uoHJJtI&feature=youtu.be

Otin videon komennolla
```
raspivid -o testivideo.h264 -w 1280 -h 720 -t 20000
```
(argumentilla `-t 15000` video oli oikeasti vain n. 10 s. pituinen. Arvolla `20000` videosta tuli n. 15 s. pituinen.)
Rajoitin videon kokoa argumenteilla `-w ja -h`.

## 3.5
Ajoin
```
crontab -e
```
Lisäsin rivin
```
0 * * * * raspistill -o /home/pi/latest.jpg
```

Nyt kuva tallentuu tasatunnein kotihakemistoon.

## 3.6
Käytin tehtävässä Pythonia ja Flaskia.
Koodi löytyy tiedostosta server-app.py.

Asennin Flaskin ja flask-cors-kirjaston:
```
pip3 install flask flask-cors
```

Asetin serverin hakemaan crontabin tasatunnein tallentaman kuvan:
```python
@app.route("/")
def helloWorld():
    try:
        img = open("../latest.jpg")
        return send_file("../latest.jpg", mimetype="image/jpg")
    except:
        return "Image doesn't exist!"
```
Lopulta asetin serverin toimimaan myös lähiverkossa:

```python
app.run(host= '0.0.0.0')
```

Nyt ohjelman pystyy ajamaan:
```
python3 server-app.py
```