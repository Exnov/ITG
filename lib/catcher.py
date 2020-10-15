from selenium import webdriver
from selenium.webdriver.firefox.options import Options #invisible
import time
import re
import requests
from bs4 import BeautifulSoup
import os
import platform

"""
===================================
Classe Catcher :
==> Elle récupère les images d'un compte insta :
	==> à partir d'urls écrites par l'utilisateur dans un fichier texte créé par la classe à sa 1ère utilisation (comptes.txt)
===================================
"""
class Catcher:

	def __init__(self):
		self.version="1.0"
		self.dateVersion="Octobre 2020"
		self.driver=None
		self.path=None
		self.classNameOne='g47SY' #classe CSS de l'elt qui affiche le nombre de publications
		self.classNameTwo="RnEpo" #classe CSS du cadre avec fenêtre de dialogue des cookies (qui obscurcit l'écran)
		self.classNameThree="dCJp8" #classe CSS du bouton qui ferme la fenêtre de dialogue pour se connecter à instagram (qui obscurcit aussi l'écran)
		self.classNameFour="tCibT" #classe CSS du bouton qui affiche les posts du bas de la page
		self.url=None
		self.urlsSpider=[]
		self.urlImgs=[]

	
	#-- Lance le programme si des urls existent dans le fichier "comptes.txt" :
	def go(self):
		self.printInfosProg()
		self.getUrlCompte()
		if(self.url):
			self.pathGecko()
			self.prog()		

	#-- En-tête avec présentation du programme : Nom, service, version, auteur :
	def printInfosProg(self):
		print("-------------ITG ------------")
		print("-- Collecte d'images sur Instagram --")
		print("Version : "+self.version)
		print("Date version : "+self.dateVersion)
		print("Date création : Octobre 2020")
		print("Auteur : Captain Looser")
		print("------------------------------\n")

	#-- Identifier l'OS pour bien se positionner dans le dossier qui contient geckodriver.exe :
	def pathGecko(self):
		osName=platform.system()
		suffixePath="/geckodriver/geckodriver.exe"
		if(osName=="Windows"): #Windows
			self.path=os.getcwd().replace("\\","/")+suffixePath
		else: #Linux et Mac
			self.path=os.getcwd()+suffixePath

	#-- Ouvre le txt qui contient les urls des comptes insta :
	"""
		==> renvoie l'url du compte choisi par l'utilisateur
		==> si url renvoyée nulle ==> le programme s'arrête	
	"""
	def getUrlCompte(self): 
		urls=[]
		compteur=0

		try:
			comptes = open("comptes.txt","r")
			urls=[]
			regex=r"https://www.instagram.com/"
		except Exception as e: #si le fichier n'existe pas, on le crée
			comptes = open("comptes.txt", "w")

		if (os.stat("comptes.txt").st_size == 0): #on lance le programme uniquement si le fichier n'est pas vide !
			print("Fichier vide !")
			print("Ajoute l'url des comptes insta qui t'intéressent dans le fichier comptes.txt (1 url par ligne)")
			print("et relance ensuite le programme, Bye !")
		else:
			print("Liste des urls enregistrées :")
			for compte in comptes:
				#si url insta correcte, on la comptabilise, et on l'ajoute aux urls à parcourir
				if(re.search(regex,compte)):				
					compteur+=1
					print(compteur,": ",compte[:-1]) #[:-1] ==> pour supprimer le saut de ligne
					urls.append(compte[:-1])

			#si urls à parcourir, on lance le programme
			if(len(urls)>0):
				#--choix d'un compte :
				nCompte=input("Donne le numéro du compte qui t'intéresse : ")
				#-- vérification si nombre, et si nombre <= au nombre de comptes
				while(nCompte.isnumeric()==False):
					nCompte=input("Donne le numéro du compte qui t'intéresse : ")
				nCompte=int(nCompte)
				if(nCompte>len(urls)):
					nCompte=1	

				self.url=urls[nCompte-1]
				print("Compte instagram choisi : ", self.url)	

			##sinon on arrête le programme en invitant l'utilisateur à revoir ses urls 
			else:
				print("Aucune url instagram trouvée dans le fichier comptes.txt")
				print("Corrige ça, et relance ensuite le programme, Bye !")
		        
		comptes.close()


	#-- Pour cliquer sur des boutons à partir de leur classe CSS :
	def clickButton(self,className):

		className="."+className
		self.driver.execute_script(" var elt = document.querySelector(arguments[0]); if(elt) elt.click();",className)


	#-- Pour retirer la fenêtre de dialogue qui fait écran à la recupération des urls des posts
	def removeScreen(self,className):
		className="."+className
		self.driver.execute_script(" var elt = document.querySelector(arguments[0]); if(elt) elt.remove();",className)


	#-- Parcours de la page à la recherche des urls des posts :
	def getUrlPosts(self,nImagesWanted):
		
		goOn=True
		i=0
		compteur=0
		regex=r"https://www.instagram.com/p/"
		last_height=0
		first_height=1

		while goOn: 

			#Gestion de la hauteur de la page, pour casser la boucle quand on arrive en bas de page
			if(last_height==first_height):
				break
				
			first_height = self.driver.execute_script("return document.body.scrollHeight")
			self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","") 
			time.sleep(0.5) #pour laisser au driver le temps de scroller la page

			for elt in self.driver.find_elements_by_tag_name("a"):
					url=elt.get_attribute("href")
					if(re.search(regex,url)):
						#on ajoute l'url seulement si elle n'est pas déjà dans la liste d'urls
						if(url not in self.urlsSpider):
							self.urlsSpider.append(url)
							#progression :
							compteur+=1
							print(compteur,"post(s) trouvé(s)")
							#si nombre d'images atteint, on casse la boucle
							if(compteur==nImagesWanted):
								goOn=False
								break
			#Gestion du scroll et de la boucle
			last_height = self.driver.execute_script("return document.body.scrollHeight")
			#---------------------------		

		self.driver.quit() 

		#Affichage d'infos dans la console pour renseigner l'utilisateur sur la progression des posts trouvés
		print("===========================\nTotal : ",len(self.urlsSpider),"post(s) trouvé(s)\n===========================\n")
		print("#url des posts :")
		c=0
		for n in self.urlsSpider:
			c+=1
			print(c," : ", n)
		print("\n")


	#-- Pour récupérer les urls des images sur la page de chaque post :
	def getUrlImgs(self):

		print("#url des images :")
		c=0
		for url in self.urlsSpider:
			try:
				html=requests.get(url) 
				soupe=BeautifulSoup(html.text,features="html.parser") #features="html.parser" ==> pour éviter message d'alerte.
				for m in soupe.find_all("meta"):
					if(m.get("property")=="og:image"):
						c+=1
						self.urlImgs.append(m.get("content"))
						print(c," : ", m.get("content"))
			except Exception as e:
				print(e) 		
		print("\n")


	#-- Pour télécharger les images à partir de leur url :
	def getImgs(self): 

		regex=r".jpg" 

		#on vérifie si les urls de la liste sont valides
		if(re.search(regex,self.urlImgs[0])): #on suppose que si la 1ère est OK, les suivantes aussi
			y=0		
			elts=len(self.urlImgs)	
			#on demande le nom à donner aux images
			nomImages=input("Nom a donner aux images ? : ")
			if(len(nomImages)==0): #si l'utilisateur donne un nom vide, "image" est le nom par défaut 
				nomImages="image"
			print("Téléchargement : nombre total d'images : ",elts)
			#gestion du dossier d'exportation, s'il n'existe pas, on le crée
			dossier=os.getcwd() +"\\"+"images"
			if(os.path.exists("images")==False):
				os.mkdir("images")
				print("Création du dossier d'exportation 'images'")
			#création du dossier d'exportation des images, simplement nommé "images"
			temps=time.localtime()
			tps_dossier=str(temps[2]) +"_"+ str(temps[1])+"_"+str(temps[0]) + "_" + str(temps[3]) + str(temps[4]) + str(temps[5]) #jour mois annee heure minute seconde
			nom_dossier=nomImages + "_" + tps_dossier
			os.mkdir("images/"+nom_dossier)
			#nommage des images et enregistrement dans le dossier "images"
			for i in range(elts): 			
				y+=1 
				img=requests.get(self.urlImgs[i]).content 
				n="" 
				if(y<10):
					n="0"+str(y)
				if(y>=10):
					n=str(y)		
				nomImg=nomImages+n+".jpg"
				with open("images/"+nom_dossier+"/"+nomImg,"wb") as handler: 
					handler.write(img)
				print(y,"/",elts)
			print("copie finie de " + n + " images dans le dossier : " + dossier)
		
		else: #si la liste des urls n'est pas bonne :
			print("La liste des urls fournies n'est pas bonne, opération annulée")


	#-- Gère toutes les opérations de récupération des images :
	#	==> Se lance uniquement si existence d'urls dans le fichier "comptes.txt"
	def prog(self):

		print("C'EST PARTI...\n")

		#invisible
		options = Options()
		options.set_headless(headless=True)

		self.driver = webdriver.Firefox(firefox_options=options,executable_path=self.path)  
		self.driver.get(self.url)

		#--Affichage du nombre de publications (photos et vidéos mélangées):
		nPosts=self.driver.find_element_by_class_name(self.classNameOne).text 
		print("===========================")
		print(nPosts, " publications")
		print("===========================")

		#retrait des élts HTML qui empêchent le scrolling de la page :
		#retrait de la fenêtre de dialogue pour les cookies :
		self.removeScreen(self.classNameTwo)
		#retrait de la fenêtre de dialogue pour se connecter à Instagram :
		self.clickButton(self.classNameThree)

		#Affichage complet de la page :
		self.clickButton(self.classNameFour)		

		#--On demande à l'utilisateur combien il veut récupérer d'images sur le nombre de publications
		nPostsWanted=input("Tu veux combien d'images ? : ")
		#-- verification si nombre, et si nombre <= au nombre de publications
		while(nPostsWanted.isnumeric()==False):
			nPostsWanted=input("Tu veux combien d'images ? : ")
		nPosts=nPosts.replace(' ', '') #on supprime les éventuels espaces vides (ex:1 000)
		nPostsWanted=int(nPostsWanted)
		if(nPostsWanted>int(nPosts)):
			nPostsWanted=nPosts
		print("On va essayer de récupérer ",nPostsWanted," images\n")

		#Récupération des urls de chaque publication
		self.getUrlPosts(nPostsWanted)

		#Récupération des urls des images
		self.getUrlImgs()

		#Téléchargement des images
		self.getImgs()