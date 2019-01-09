# Demo 1

## Tehtävä 1.1
1. Loin GitHub-repon.

## Tehtävä 1.4 (tein tämän kohdan ensimmäisenä!)
1. Latasin Raspbian Liten imagen Raspbian kotisivuilta: https://www.raspberrypi.org/downloads/raspbian/
2. Latasin Etcher-nimisen työkalun imagen kirjoitusta varten: https://www.balena.io/etcher/
3. Asetin SD-kortin lukijaan ja valitsin Etcherissä Raspbian Liten zip-tiedoston ja kohteeksi SD-kortin.
4. Ohjelma alusti kortin ja kirjoitti imagen kortille.
5. Loin SD-kortin `boot`-osiolle tiedoston nimeltä "ssh" (että Raspbian sallisi SSH-yhteydet oletuksena)
6. Jatkoin tehtävän 1.2 parissa.

## Tehtävä 1.2 - Raspbian
1. Asetin MicroSD-kortin Raspiin ja kytkin sen lähiverkkooni Ethernet-kaapelilla.
2. Tarkistin reitittimen nettikäyttöliittymästä minkä IP:n DHCP oli antanut Raspille: `192.168.1.3`
3. Avasin Kitty-nimisen SSH-clientin. Yhdistin edellämainittuun IP:seen ja kirjauduin sisään oletustunnuksilla: `pi` ja `raspberry`.
4. Vaihdoin oletussalasanan komennolla `passwd`
5. Ajoin Raspin konfiguraatiotyökalun: `sudo raspi-config`.
6. Asetin timezonen (Helsinki), localen (fi-UTF8), keyboardin (fi) ja wificountryn. (Etäyhteyttä ei tarvinnut enabloida, tein sen jo samalla kun kirjoitin Raspbian Liten imagen kortille.)
7. Yhdistin wifi-verkkoon raspi-configin avulla. Tarkistin vielä, että sain IP:n `ifconfig`in avulla.
8. Hoidin päivitykset:
    ```bash
    sudo apt-get update
    sudo apt-get dist-upgrade
    ```
9. Reboottasin Raspin komennolla `sudo reboot`.
10. Otin Ethernet-kaapelin irti ja kokeilin, toimiiko SSH-yhteys wifin yli. (Kyllä toimii!)

## Tehtävä 1.3: SSH-yhteys
(Tämä tehtävä tuli tehtyä tehtävien 1.4 ja 1.2 aikana!)
1. Loin SD-kortin `boot`-osiolle tiedoston nimeltä "ssh" (että Raspbian sallisi SSH-yhteydet oletuksena)
2. Asetin MicroSD-kortin Raspiin ja kytkin sen lähiverkkooni Ethernet-kaapelilla.
3. Tarkistin reitittimen nettikäyttöliittymästä minkä IP:n DHCP oli antanut Raspille: `192.168.1.3`
4. Avasin Kitty-nimisen SSH-clientin. Yhdistin edellämainittuun IP:seen ja kirjauduin sisään oletustunnuksilla: `pi` ja `raspberry`.