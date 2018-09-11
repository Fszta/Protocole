# Protocole
Test de stroop + capteur PPG + capteur gsr + caméra 
<br/> https://fszta.github.io/Protocole/
<p>
  <h2>Objectifs</h2>
  Protocole visant à induire un stress chez les participants dans le but d'obtenir des mesures physiologiques de personnes en état                de stress et en état de relaxation. Le but final étant de créer un modèle de classification du stress à partir de ces données, modèle qui classifiera les données selon deux groupes : stressé / relaxé. Le deuxième intérêt est d'avoir un signal PPG issu d'un capteur synchronisé avec la vidéo du visage pour valider notre système de mesure de l'activité cardiaque par caméra.
  Le protocole dure 389 secondes, il est composé de trois phases de relaxation (vidéo de paysage) et de trois phases de stress (test de stroop). Pour chaque participant, nous disposerons de :
  <ul>
  <li>Signal photopléthysmographique (mesure les variations du volumes sanguins dans les tissus)</li>
  <li>Signal gsr (mesure les variations de la conductimétrie de la peau ~ la sudation)</li>
  <li>Vidéo du visage du participant (que l'on utilisera pour extraire le signal PPG et valider notre système de mesures</li>
  </ul>
</p>

<h2>Système</h2>
<ul>
  <li>Un raspberry avec une Picamera</li>
  <li>Un raspberry avec les deux capteurs, communication SPI pour le capteur PPG, I2C pour le capteur GSR</li>
  <li>Les deux raspberry sont reliés via GPIO</li>
</ul>

<h2>Fonctionnement</h2>
<ul>
  <li>Tester les capteurs et la position du participant dans le champ de la caméra avec les codes test</li>
  <li>Sur le Raspberry1 avec la caméra : Lancer le code record.py en parsant le numéro du participant</li>
  <li>record.py check l'état du GPIO 12 toutes les 0.5 seconde. Rien ne se passe tant que GPIO 12 à 0</li>
  <li>Sur le Raspberry2 avec les capteurs : Lancer le code physiologic_signals.py en parsant le numéro du participant</li>
  <li>Le GPIO 16 du Raspberry2 est forcé à 1 et met à 1 le GPIO 12 du Raspberry1</li>
  <li>L'enregistrement vidéo et l'acquisition des données des capteurs démarre, la vidéo du protocole démarre</li>
</ul>

<h2>Usage</h2>
<h4>Argument parser:</h4>
<ul>
  <li>1-record.py N°participant</li>
  <li>2-physiologic_signals.py N°participant</li>
</ul>

<h2>Librairies</h2>
<ul>
  <li>spidev==3.3</li>
  <li>RPi.GPIO==0.6.3</li>
  <li>smbus-cffi==0.5.1</li>
  <li>scipy==1.0.1</li>
  <li>numpy==1.13.3</li>
  <li>picamera==1.13</li>
  <li>matpotlib==2.2.2</li>
</ul>

<h2>Codes</h2>
<ul>
  <li>gsr_sensor.py : code capteur de conductance cutanée</li>
  <li>ppg_sensor.py : code capteur photopléthysmographique</li>
  <li>MCP3008.py : code convertisseur analogique numérique</li>
  <li>record_capture.py : code enregistrement vidéo</li>
  <li>physiologic_signals.py : code lancement mesures, vidéo et enregistrement</li>
  <li>test_gpio.py : code test état GPIO</li>
  <li>test_record.py : code test engistrement caméra</li>
  <li>test_sensors.py : code test de la position des capteurs</li>
</ul>
