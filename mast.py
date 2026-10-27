# on importe pygame, random et le module mm.py
import pygame
import random
import mm


pygame.init()


def genererCombinaison():
    """
    Cette fonction permet de générer la combinaison secrète.
    """
    secret = []

    for i in range(5):
        secret.append(mm.TabCouleur[random.randint(0, 7)])

    return secret

test = genererCombinaison()
print(test)
print(len(test))

def calculresultat(proposition, secret):
    """
    Cette fonction calcule le nombre de pions bien placés
    et le nombre de pions mal placés.
    """

    bien = 0
    pasbien = 0

    combinaison_temp = list(secret)

    # recherche des pions bien placés
    for i in range(5):
        if proposition[i] == secret[i]:
            bien = bien + 1
            combinaison_temp[i] = None

    # recherche des pions mal placés
    for elt in proposition:
        if elt in combinaison_temp:
            pasbien = pasbien + 1
            position = combinaison_temp.index(elt)
            combinaison_temp[position] = None

    return bien, pasbien


def afficherMessage(f: pygame.Surface, message: str) -> None:
    """
    Cette fonction affiche un message à l'écran.
    """
    myfont = pygame.font.SysFont("monospace", 20)
    label = myfont.render(message, 1, mm.Noir)

    f.blit(label, (100, 700))
    pygame.display.update()


# création de la fenêtre
laFenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mastermind")

laFenetre.fill(mm.Blanc)

# affichage du plateau et des couleurs
mm.afficherPlateau(laFenetre)
mm.afficherChoixCouleur(laFenetre)


# génération de la combinaison secrète
secret = genererCombinaison()


# jeu : 15 essais maximum
for ligne in range(2, 17):

    # le joueur construit sa proposition
    proposition = mm.construireProposition(laFenetre, ligne)

    # calcul du résultat
    resultat = calculresultat(proposition, secret)

    # affichage du résultat
    mm.afficherResultat(laFenetre, resultat, ligne)

    # si la proposition est correcte
    if proposition == secret:
        mm.afficherSecret(laFenetre, secret)

        message = f"Félicitations ! Vous avez gagné en {ligne - 1} coups !"
        afficherMessage(laFenetre, message)

        break

    # si c'était le dernier essai
    if ligne == 16:
        mm.afficherSecret(laFenetre, secret)

        message = "Désolé, vous avez perdu."
        afficherMessage(laFenetre, message)


# attente avant de fermer
fini = False

while not fini:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                fini = True

        if event.type == pygame.QUIT:
            fini = True


pygame.quit()