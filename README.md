# Protocole
Test de stroop + capteur PPG + capteur gsr + caméra 
<p>
  <h2>Objectifs</h2>
  Protocole visant à induire un stress chez les participants dans le but d'obtenir des mesures physiologiques de personnes en état                de stress et en état de relaxation. Le but final étant de créer un modèle de classification du stress à partir de ces données, modèle classifiera les données selon deux groupes : stressé / relaxé 
</p>


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
