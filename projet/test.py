# on import les packages nécessaire :
# opencv pour le lecteur vidéo et la decetion faciale
# ffpyplayer pour le son de la vidéo
# tkinter pour l'interface graphique et lire le fichier ".mp4"
# enfin os pour determiner le chemin dans lequel on travail
import cv2
import os
os.chdir(r"C:\Users\maroc\Desktop\ECOLE\projet")
from ffpyplayer.player import MediaPlayer
from tkinter import *
from tkinter import filedialog

# création de la fenetre et definition du fichier stockage
fenetre = Tk()
fenetre.geometry("1280x720")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# fonction file() en tkinter qui permet d'importer des fichiers en format mp4 et qui lance PlayVideo() avec comme argument  la vidéo en mp4, renvoie une erreur si aucune fichier n'a été selectionné
def file():
    var =  filedialog.askopenfilename(title = "Select file",filetypes = (("mp4 files",".mp4"),("all files",".*")))
    if var != '':
        fenetre.destroy()
        PlayVideo(var)
    else:
        print('tu na pas mis de fichier')


# fonction Playvidéo() qui prend en argument la vidéo a lire en ".mp4".
# On commence avec un try/ except pour éviter les bug afficher dans la console a la fin de la vidéo. dans les variables video et player on crée l'outil de capture a utiliser et le son de cette outils de capute en ".mp4" ensuite pour étudier la detection faciale on utilse une boucle infinie qui tourne tant que la vidéo n'est pas fini grace au try.Dans cette boucle infinie on lie le son a la vidéo. Puis on utilise le fichier cascade défini précedemment pour detecter les visages. On definie la couleur du rectangle dans la variable gray puis on fait une boucle pour les dimensions du rectangle.
# La deuxieme partie du la fonction nous permet de fermer la fenetre a l'aide de la touche "f" du clavier et de mettre pause au son et a la vidéo avec la touche p.
def PlayVideo(video_path):
    try:
#     image
        video=cv2.VideoCapture(video_path)
    #      son
        player = MediaPlayer(video_path)
        while True:
            grabbed, frame=video.read()
            audio_frame, val = player.get_frame()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            key = cv2.waitKey(1)
            if key == ord("f"):
                break
            if key == ord('p'):
                cv2.waitKey(-1)
                player.toggle_pause()
            cv2.imshow("MediaPlayer", frame)
        video.release()
        cv2.destroyAllWindows()
    except:
        pass


# Configuration de l'interface graphique
bouton = Button(fenetre, text="Selectionner ",fg='white', bg='purple', font=('comicsans', 10),command=file)
bouton.place(x=640,y=360)
fenetre.mainloop()
