
def contar_vocales(texto):
    """Cuenta el número de vocales en el texto."""
    return sum(1 for c in texto.lower() if c in "aeiou")

if __name__ == "__main__":
    texto = "Hola mundo"
    print(f'El texto "{texto}" tiene {contar_vocales(texto)} vocales.')
