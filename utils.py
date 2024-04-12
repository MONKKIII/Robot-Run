import pickle

SCORE_FILE = "score_data.txt"

def save_score(score):
    with open(SCORE_FILE, "a") as file:
        file.write(str(score) + "\n")

def load_scores():
    try:
        with open(SCORE_FILE, "r") as file:
            scores = [int(score.strip()) for score in file.readlines()]
            scores.sort(reverse=True)  # Tri des scores dans l'ordre décroissant
            return scores
    except FileNotFoundError:
        return []

# Fonction pour effacer toutes les données du fichier score_data.txt
def delete_score_data():
    try:
        with open(SCORE_FILE, "w") as file:
            file.truncate(0)  # Efface le contenu du fichier
    except FileNotFoundError:
        pass