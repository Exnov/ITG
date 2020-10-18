# ITG
ITG collecte des images sur Instagram

## Version information

#### Version 1.0

## Méthode 1 : via l'exécutable 
### Nécessités
- itg.exe
- geckodriver.exe de Mozilla

### Installation
- Téléchargez itg.zip, et décompressez le fichier
- Téléchargez geckodriver.exe (voir section 'Téléchargement de geckodriver.exe depuis GitHub')

### Utilisation
- Cliquez sur itg.exe
- Suivez les instructions du programme
- Si vous cherchez 'comptes.txt', vous le trouverez dans le dossier 'ITG'

## Méthode 2 : via le script python
### Nécessités
- Un terminal
- Python (version >=3.6.5)
- Les outils Pythons suivants : Selenium, Beautifulsoup, et Requests
- geckodriver.exe de Mozilla

### Installation
#### Téléchargement de nos 3 outils Python (pour ceux qui ne les ont pas bien sûr) à coup de pip dans le terminal :
```
pip install selenium
pip install beautifulsoup4
pip install requests 
```

#### Téléchargement de ITG depuis GitHub :
- Créez un nouveau dossier sur votre PC pour recevoir ITG ; nommez-le comme vous voulez
- RDV dedans avec votre terminal :
```
cd chemin\vers\monsuperprogramme
```
- On télécharge ITG dans ce dossier :
```
git clone https://github.com/Exnov/ITG.git
```
Si vous n'avez pas la commande 'git', téléchargez le ZIP du code de ITG, qui se trouve en haut de cette page (bouton vert 'Code', puis 'Download ZIP')

C'est presque fini, reste à télécharger geckodriver.exe (voir section 'Téléchargement de geckodriver.exe depuis GitHub'). Une fois que c'est OK, vous pouvez passer à la section 'Utilisation'

### Utilisation 
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
- Suivez ensuite les instructions du programme pour collecter vos images Instagram préférées
- Si vous cherchez 'comptes.txt', vous le trouverez dans le dossier 'ITG'

## Téléchargement de geckodriver.exe depuis GitHub :
- On rentre dans le dossier 'ITG', et on y crée le sous-dossier 'geckodriver' pour recevoir geckodriver.exe
- Allez sur la page GitHub de Mozilla dédiée à son driver : https://github.com/mozilla/geckodriver/releases
- Téléchargez la dernière version de geckodriver.exe qui colle à votre OS
- Décompressez le fichier et copiez geckodriver.exe dans le dossier 'geckodriver'

C'est tout !
