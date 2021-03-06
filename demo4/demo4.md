# Demo 4

## 4.1 Motionin asennus (1p)
Ensiksi ajoin:
```
sudo apt-get update
sudo apt-get install motion -y

mkdir motion    
sudo cp /etc/motion/motion.conf ~/motion/motion.conf  
sudo chown pi:pi motion/motion.conf
```
Ks. motion_t_4_1.conf

## 4.2 Kuvia ennen liikettä (1p)
Asetin
```
pre_capture 2
post_capture 10
```
Koska framerate on max 2 framea / sekunti,
pitäisi tuolla arvolla kuvia tulla n. 5 sek liikkeen jälkeen.

Ks. motion_t_4_2.conf

## 4.4 Keskusta (2p)
Loin Gimpillä maskikuvan ja siirsin sen Raspille.

PGM-kuva: https://drive.google.com/open?id=13pbY0ykMyrVrGZb5IAMswvY9qrlhJeGL

JPG-kuva: https://drive.google.com/open?id=1mlKR0bpVZeQ4X7NnNXFPcX2XmWKmKm_e

Configgiin seuraavat muutokset:
```
mask_file /home/pi/motion/motion-mask.pgm
```

Ks. motion_t_4_4.conf

## 4.5 OpenCV:n asentaminen (2p)

Asensin OpenCV v. 4.0.0:n netistä löytyneillä ohjeilla:

Ajoin:
```
sudo apt-get install build-essential cmake unzip pkg-config
```
sitten:
```
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
```
Netissä suositeltiin asentamaan myös nämä:
```
sudo apt-get install libatlas-base-dev gfortran
```
Python3 dev-headerit:
```
sudo apt-get install python3-dev
```
Latasin OpenCV:n:
```
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
```

Purin paketit ja nimesin kansiot uudelleen:
```
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.0.0 opencv
mv opencv_contrib-4.0.0 opencv_contrib
```
Asensin tarvitut Python-kirjastot ja loin uuden virtual environmentin:
```
sudo pip3 install virtualenv virtualenvwrapper

# Lisäsin ~/.profile -tiedostoon:

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
...
source ~/.profile
```
sitten: `mkvirtualenv cv -p python3`.

Asensin matplotlib ja NumPy:n:
```
pip3 install numpy
pip3 intall matplotlib --no-cache
```
Valmistelin OpenCV:n kääntämisen:
```
cd ~/opencv
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
```

Muokkasin CONF_SWAPSIZE-muuttujaa /etc/dphys-swapfile-tiedostossa ja kasvatin swap-tiedoston kokoa. Se mahdollistaa
kääntämisen neljällä ytimellä.
```
sudo nano /etc/dphys-swapfile

# tiedostossa:
...
CONF_SWAPSIZE=2048
...
```
Uudelleenkäynnistin swap-palvelun.

Nyt oli aika kääntää OpenCV:

```
make -j4 // -j4-argumentti asettaa kääntäjän käyttämään neljää ydintä.
// reilut 2 tuntia myöhemmin..
sudo make install
sudo ldconfig
```
Linkataan OpenCV luomaamme Python-virtuaaliympäristöön:
```
cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/python/cv2/python-3.5/cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so
```

Kokeillaan, että asennus onnistui:
```
(cv) pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'4.0.0'
```