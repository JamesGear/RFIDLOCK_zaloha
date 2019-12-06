# RFID zámek 
Jako závěrečný projekt jsem si vybral systém zámků na dveře s odemykáním pomocí RFID chipu/karty, pro práci jsem si zvolil mikrokontroler ESP8266. Rozhodl jsem po domluvě s p. učitelem Grussmannem pro využití technologií: MQTT; Mosquitto; Flask bones; Docker; Yarn 
## Základní princip: 
Uživatel přiloží RFID kartu ke čtečce u dveří, po přiložení se ESP probudí a odešle přes wifi požadavek na server ve kterém se ověří jestli je uživatel registrovaný, patří do skupiny firmy a má-li časový přístup, pokud vše ověří a výsledek je kladný, pošle se zpátky signál, který otevře dveře. 
## Reference: 
https://www.instructables.com/id/TfCD-NFC-Beer-Lockbox/ zámek dveří na NFC 

https://www.makeuseof.com/tag/diy-smart-lock-arduino-rfid/ zámek dveří na RFID 

https://3dprint.com/53583/nfc-door-lock-qduino-mini/ zámek dveří při využití arduina 

https://bbs.espressif.com/viewtopic.php?t=133 https://github.com/petrgru/karty RFID chipy fungující na škole 

https://www.root.cz/clanky/protokol-mqtt-komunikacni-standard-pro-iot/ základní zprovoznění MQTT protokolu 

https://iotta.cz/esp8266-mqtt/ propojení ESP a MQTT 

http://www.steves-internet-guide.com/into-mqtt-python-client/ nastavení MQTT pro python 

https://test.mosquitto.org/ veřejný Mosquitto server 
## Potřebné díly: 
Elektrický zámek dveří 

RFID čtečka 

ESP8266 

Pole na pájení 

Kabely 

Bzučák 

RFID chip/karta 
## Instalace Flask Bones 

   1. Nainstalujeme Docker pro windows (https://hub.docker.com/editions/community/docker-ce-desktop-windows) 

   2. Docker musí být nastavený na “Linux constainers” 

   3. Sdílení disků musí být povoleno 

   4. Poté stáhneme a nainstalujeme PostrgreSQL (https://www.postgresql.org/download/) 

   5. PostgreSQL si automaticky nastaví server na adresu localhost:5432 

   6. Dále si stáhneme a nainstalujeme vývojové prostředí Pycharm (pozn. Pycharm musí být v professional verzi, kvůli nastave propojení s Dockerem, Community verze tuto možnost bohužel nenabízí) 

   7. V pycharmu si otevřeme flask bones (originální autor : https://github.com/cburmeister/flask-bones) 

   8. V projektu si jako Interpreter nastavíme docker 

   9. Poté použijeme příkaz : 

```bash
docker-compose up -d
```
   10. Dále nainstalujeme Yarn :
   
```bash
yarn install --modules-folder ./app/static/node_modules 
```
