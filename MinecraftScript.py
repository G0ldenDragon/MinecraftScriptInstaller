

# .EXE CREATED USING pyinstaller --clean -F MinecraftScript.py


from os import getenv as os_getenv, path as os_path, getcwd as os_getcwd
from urllib.request import urlretrieve
from subprocess import run as subprocess_run, Popen as subprocess_Popen
from json import load as json_load


appdata_path = os_getenv('APPDATA')
minecraft_path = appdata_path + '\\.minecraft'
mods_path = minecraft_path + '\\mods'

def waiting_answer(message: str= "Pour continuer le script, écrire 'ok' puis appuyer sur la touche 'Entrée'...") -> bool:
    while True:
        print(message)
        answer = input("--> ")
        if answer.lower() == "ok" or answer.lower() == "oui":
            return True
        elif answer.lower() == "non":
            return False


try:
    with open("installer.json", "r") as file:
        data = json_load(file)

        SCRIPT_VERSION = data["SCRIPT_VERSION"]
        JAVA_INSTALLER = data["JAVA_INSTALLER"]
        MINECRAFT_INSTALLER = data["MINECRAFT_INSTALLER"]
        FABRIC_INSTALLER = data["FABRIC_INSTALLER"]
        MINECRAFT_VERSION = data["MINECRAFT_VERSION"]

except FileNotFoundError as e:
    print(f"Le fichier de installer 'installer.json' est introuvable. Veuillez le copier dans ce dossier puis pour relancer le script en passant les étapes précédentes.")
    waiting_answer("Si les instructions ont été suivies, écrire 'ok' puis appuyer sur la touche 'Entrée' pour fermer le script...")
    exit()
    

# ------------------------------------------------------------


print(f"""VERSION {SCRIPT_VERSION}\nBienvenue dans le script d'installation de Minecraft Java Edition avec mods.""")
print("""ATTENTION : Si le script ne semble pas avancer, vérifier que le titre de la fenêtre du script ne contient PAS "Select", si c'est le cas, appuyer à l'intérieur de la fenêtre du script puis appuyer sur la touche 'Entrée' pour continuer le script.""")


java_installer = "java-installer.exe"
print("""\n\n➡️  Le fichier d'installation de JAVA (nécessaire à l'utilisation de Minecraft Java) est en cours de téléchargement...
Le temps d'attente est long et peut durer quelque minutes. Veuillez patienter, merci de ne pas fermer ce script.""")
if not os_path.exists(java_installer):
    urlretrieve(JAVA_INSTALLER, java_installer)

print(f"""Le fichier d'installation de JAVA a été téléchargé avec le nom --{java_installer}--.
Merci d'ouvrir en tant qu'ADMINISTRATEUR pour effectuer l'installation puis cliquer sur 'Install'.
Pour ouvrir en tant qu'ADMINISTRATEUR, faites un clic DROIT sur le fichier et sélectionnez 'Exécuter en tant qu'administrateur'.""")
full_path = os_path.join(os_getcwd(), java_installer)
subprocess_Popen(rf'explorer /select, {full_path}')
waiting_answer()



minecraft_installer = "minecraft-installer.exe"
print("""\n\n\n➡️  Le fichier d'installation de MINECRAFT est en cours de téléchargement...
Le temps d'attente est long et peut durer quelque minutes. Veuillez patienter, merci de ne pas fermer ce script.""")
if not os_path.exists(minecraft_installer):
    urlretrieve(MINECRAFT_INSTALLER, minecraft_installer)

print(f"Le fichier d'installation de MINECRAFT a été téléchargé avec le nom --{minecraft_installer}--.")
print(f"""Dans l'installateur, veuillez vous connecter à un compte Microsoft ayant une clé/copie de Minecraft. Puis, 
1 - Se rendre dans 'Minecraft: JAVA EDITION' dans la partie gauche de l'écran. 
2 - Sélectionner 'Configuration' dans la partie haute de l'écran.
3 - Appuyer sur 'Nouvelle configuration'.
4 - Dans 'Nom', mettre '{MINECRAFT_VERSION}'.
5 - Dans 'Version', sélectionner 'release {MINECRAFT_VERSION}'.
6 - Cocher 'Lancer après l'installation'.
7 - Cliquer sur 'Installer'.
8 - Attendre que le jeu se lance, puis fermer le jeu et l'installateur.""")
subprocess_run(minecraft_installer, check=True)
waiting_answer()



fabric_installer = "fabric-installer.exe"
print("""\n\n\n➡️  Le fichier d'installation de FABRIC (nécessaire pour permettre l'ajout de mods) est en cours de téléchargement...
Le temps d'attente est long et peut durer quelque minutes. Veuillez patienter, merci de ne pas fermer ce script.""")
if not os_path.exists(fabric_installer):
    urlretrieve(FABRIC_INSTALLER, fabric_installer)

print(f"Le fichier d'installation de FABRIC a été téléchargé avec le nom --{fabric_installer}--.")
print(f"""Dans la fenêtre qui s'affiche :
1 - Pour 'Minecraft Version', sélectionner '{MINECRAFT_VERSION}'.
2 - Cocher la case 'Create profile' pour quelle soit en BLEU
3 - Cliquer sur 'Install'.

ATTENTION : Si une pop-up avec pour titre "Minecraft launcher is open" s'ouvre : 
1 - Sélectionner 'No'.
2 - Fermer l'application Minecraft et/ou Minecraft Launcher.
3 - Cliquer une nouvelle fois sur 'Install' dans l'installateur de FABRIC.

Si tout se passe bien, un message de confirmation s'affichera avec pour titre "Successfully Installed". 
Vous pouvez cliquer sur "OK" et fermer l'installateur de FABRIC.
""")
subprocess_run(fabric_installer, check=True)
waiting_answer()


# Mods installation
ModsAndOtherScript = "ModsAndOtherScript.exe"
subprocess_run(ModsAndOtherScript, check=True)


print(f"""Version moddée intégralement préparée pour la version {MINECRAFT_VERSION} avec FABRIC et les mods, shaders et ressources packs téléchargés.
\nDans le Launcher Minecraft qui s'ouvre, sélectionnez la version "fabric-loader-{MINECRAFT_VERSION}" puis cliquez sur "Jouer" pour lancer le jeu.""")
subprocess_run(minecraft_installer, check=False)

waiting_answer("Pour fermer ce script, écrire 'ok' puis appuyer sur la touche 'Entrée'...")
exit()
