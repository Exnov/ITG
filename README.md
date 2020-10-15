# ITG
ITG collecte des images sur Instagram.

## Version information

#### Version 1.0

## Nécessités
- Python (version >=3.6.5)
- Les outils Pythons suivants : Selenium, Beautifulsoup, et Requests
- geckodriver.exe de Mozilla
- Un terminal

## Installation
### Téléchargement de nos 3 outils Python (pour ceux qui les ont pas bien sûr) à coup de pip dans le terminal :
```
pip install selenium
pip install beautifulsoup4
pip install requests 
```

### Téléchargement de ITG depuis GitHub :
- Créez un nouveau dossier sur votre PC pour recevoir ITG ; nommez-le comme vous voulez.
- RDV dedans avec votre terminal :
```
cd chemin\vers\monsuperprogramme
```
- On télécharge ITG dans ce dossier :
```
git clone https://github.com/Exnov/ITG.git
```
Si vous n'avez pas la commande 'git', téléchargez la version zip de ITG qui se trouve en haut de cette page (bouton vert 'Code', puis 'Download ZIP')
- On rentre dans le dossier ITG, et on y crée le sous-dossier 'geckodriver' pour recevoir geckodriver.exe :
```
cd ITG
mkdir geckodriver
```
C'est presque fini, reste à télécharger geckodriver.exe.

### Téléchargement de geckodriver.exe depuis GitHub :
- Allez sur la page GitHub de Mozilla dédiée à son driver : : https://github.com/mozilla/geckodriver/releases
- Téléchargez la dernière version de geckodriver.exe qui colle à votre OS.
- Décompressez le fichier et copiez geckodriver.exe dans notre dossier 'geckodriver'.

Installation terminée !

## Utilisation 
- Allez dans le dossier de ITG avec votre terminal :
```
cd chemin\vers\ITG
```
- Lancez le programme avec la commande suivante sur Windows :
```
itg
```
- Et la commande suivante pour les autres OS :
```
itg.py
```
- Suivez ensuite les instructions du programme pour collecter vos images Instagram préférées.

C'est tout !
