def convertir_note(texte):
    try:
        return float(texte.replace(",", "."))
    except ValueError:
        return None
    

def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)