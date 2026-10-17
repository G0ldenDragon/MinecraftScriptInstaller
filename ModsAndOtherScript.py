from os import getenv as os_getenv, path as os_path, listdir as os_listdir, mkdir as os_mkdir
from shutil import copytree as shutil_copytree, rmtree as shutil_rmtree
from time import strftime as time_strftime, localtime as time_localtime
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor, as_completed as concurrent_futures_as_completed



appdata_path = os_getenv('APPDATA')
minecraft_path = appdata_path + '\\.minecraft'
mods_path = minecraft_path + '\\mods'
shaders_path = minecraft_path + '\\shaderpacks'
ressource_packs_path = minecraft_path + '\\resourcepacks'

def waiting_answer(message: str= "Pour continuer le script, écrire 'ok' puis appuyer sur la touche 'Entrée'...") -> bool:
    while True:
        print(message)
        answer = input("--> ")
        if answer.lower() == "ok" or answer.lower() == "oui":
            return True
        elif answer.lower() == "non":
            return False

# Not only mods, but also shaders and resource packs can be downloaded using this function.
def mod_downloader(url: str, mods_path: str, extension: str=".jar"):
    filename = None
    for segment in url.strip().split('/'):
        if extension in segment:
            filename = segment.split(extension)[0] + extension

    if not filename:
        print("Error: Could not determine filename from URL.")

    file_path_and_name = mods_path + "\\" + filename
    if not os_path.exists(file_path_and_name):
        urlretrieve(url, file_path_and_name)
    print(f"✅ Fichier {filename} téléchargé depuis {url.strip()}.")


# ------------------------------------------------------------


print("""Script de téléchargement des mods, shaders et ressources packs....""")

print("""\n\n\n➡️  Téléchargement et mise en place des MODS en cours...
ATTENTION : Cela va prendre du temps selon le nombre de mods à télécharger et la vitesse de votre connexion internet. Veuillez patienter, merci de ne pas fermer ce script.""")
if os_path.exists(mods_path) and os_listdir(mods_path) != []:
    if waiting_answer("Un dossier de mods existe déjà. En faire une sauvegarde ? \nRépondre par 'oui' ou 'non' puis appuyer sur la touche 'Entrée'..."):
        current_time = time_strftime("%Y-%m-%d_%H-%M-%S", time_localtime())
        shutil_copytree(mods_path, minecraft_path + '\\mods_BACKUP_' + current_time)
        print(f"""Un dossier de sauvegarde des mods actuels a été créé avec le nom --mods_BACKUP_{current_time}-- au chemin suivant "{minecraft_path}".""")

shutil_rmtree(mods_path, ignore_errors=True)
os_mkdir(mods_path)

try:
    with open("mods.txt", "r") as fp:
        lines = len(fp.readlines())
        print(f"Nombre de mods à télécharger : {lines}")

    with open("mods.txt", "r") as fp:
        with ThreadPoolExecutor(max_workers= 10) as executor:
            futures = []
            for url in fp:
                futures.append(
                    executor.submit(
                        mod_downloader,
                        url, 
                        mods_path
                    )
                )
            for future in concurrent_futures_as_completed(futures):
                pass

except FileNotFoundError as e:
    print(f"Le fichier de mods 'mods.txt' est introuvable. Veuillez le copier dans ce dossier puis pour relancer le script en passant les étapes précédentes.")
    waiting_answer("Si les instructions ont été suivies, écrire 'ok' puis appuyer sur la touche 'Entrée' pour fermer le script...")
    exit()



print("""\n\n\n➡️  Téléchargement et mise en place des SHADERS en cours...
ATTENTION : Cela va prendre du temps selon le nombre de shaders à télécharger et la vitesse de votre connexion internet. Veuillez patienter, merci de ne pas fermer ce script.""")
if os_path.exists(shaders_path) and os_listdir(shaders_path) != []:
    if waiting_answer("Un dossier de shaders existe déjà. En faire une sauvegarde ? \nRépondre par 'oui' ou 'non' puis appuyer sur la touche 'Entrée'..."):
        current_time = time_strftime("%Y-%m-%d_%H-%M-%S", time_localtime())
        shutil_copytree(shaders_path, minecraft_path + '\\shaderpacks_BACKUP_' + current_time)
        print(f"""Un dossier de sauvegarde des shaders actuels a été créé avec le nom --shaderpacks_BACKUP_{current_time}-- au chemin suivant "{minecraft_path}".""")

shutil_rmtree(shaders_path, ignore_errors=True)
os_mkdir(shaders_path)

try:
    with open("shaders.txt", "r") as fp:
        lines = len(fp.readlines())
        print(f"Nombre de shaders à télécharger : {lines}")

    with open("shaders.txt", "r") as fp:
        with ThreadPoolExecutor(max_workers= 10) as executor:
            futures = []
            for url in fp:
                futures.append(
                    executor.submit(
                        mod_downloader,
                        url, 
                        shaders_path,
                        ".zip"
                    )
                )
            for future in concurrent_futures_as_completed(futures):
                pass

except FileNotFoundError as e:
    print(f"Le fichier de shaders 'shaders.txt' est introuvable. Veuillez le copier dans ce dossier puis pour relancer le script en passant les étapes précédentes.")
    waiting_answer("Si les instructions ont été suivies, écrire 'ok' puis appuyer sur la touche 'Entrée' pour fermer le script...")
    exit()



print("""\n\n\n➡️  Téléchargement et mise en place des RESSOURCE PACKS en cours...
ATTENTION : Cela va prendre du temps selon le nombre de ressource packs à télécharger et la vitesse de votre connexion internet. Veuillez patienter, merci de ne pas fermer ce script.""")
if os_path.exists(ressource_packs_path) and os_listdir(ressource_packs_path) != []:
    if waiting_answer("Un dossier de ressource packs existe déjà. En faire une sauvegarde ? \nRépondre par 'oui' ou 'non' puis appuyer sur la touche 'Entrée'..."):
        current_time = time_strftime("%Y-%m-%d_%H-%M-%S", time_localtime())
        shutil_copytree(ressource_packs_path, minecraft_path + '\\resourcepacks_BACKUP_' + current_time)
        print(f"""Un dossier de sauvegarde des ressource packs actuels a été créé avec le nom --resourcepacks_BACKUP_{current_time}-- au chemin suivant "{minecraft_path}".""")

shutil_rmtree(ressource_packs_path, ignore_errors=True)
os_mkdir(ressource_packs_path)

try:
    with open("ressource_packs.txt", "r") as fp:
        lines = len(fp.readlines())
        print(f"Nombre de ressource packs à télécharger : {lines}")

    with open("ressource_packs.txt", "r") as fp:
        with ThreadPoolExecutor(max_workers= 10) as executor:
            futures = []
            for url in fp:
                futures.append(
                    executor.submit(
                        mod_downloader,
                        url, 
                        ressource_packs_path,
                        ".zip"
                    )
                )
            for future in concurrent_futures_as_completed(futures):
                pass

except FileNotFoundError as e:
    print(f"Le fichier de ressource packs 'ressource_packs.txt' est introuvable. Veuillez le copier dans ce dossier puis pour relancer le script en passant les étapes précédentes.")
    waiting_answer("Si les instructions ont été suivies, écrire 'ok' puis appuyer sur la touche 'Entrée' pour fermer le script...")
    exit()


print("""\n\nFin des téléchargements, des installations et de la mise en place des mods, shaders et ressources packs.""")