def convertir_note(texte):
    try:
        return float(texte.replace(",", "."))
    except ValueError:
        return None