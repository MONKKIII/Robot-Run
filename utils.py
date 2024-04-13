import pickle

SCORE_FILE = "score_data.txt"

def save_score(score):
    """
    Sauvegarde le score dans le fichier score_data.txt.

    Args:
        score (int): Le score à sauvegarder.
    """
    with open(SCORE_FILE, "a") as file:
        file.write(str(score) + "\n")

def load_scores():
    """
    Charge les scores à partir du fichier score_data.txt.

    Returns:
        list: Liste des scores chargés à partir du fichier, triés par ordre décroissant.
    """
    try:
        with open(SCORE_FILE, "r") as file:
            scores = [int(score.strip()) for score in file.readlines()]
            scores.sort(reverse=True)  # Tri des scores dans l'ordre décroissant
            return scores
    except FileNotFoundError:
        return []

def delete_score_data():
    """
    Efface toutes les données du fichier score_data.txt.
    """
    try:
        with open(SCORE_FILE, "w") as file:
            file.truncate(0)  # Efface le contenu du fichier
    except FileNotFoundError:
        pass
