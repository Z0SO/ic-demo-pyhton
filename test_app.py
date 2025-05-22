from app import contar_vocales

def test_contar_vocales():
    assert contar_vocales("hola") == 2
    assert contar_vocales("Python") == 1
    assert contar_vocales("AEIOU") == 5
    assert contar_vocales("xyz") == 0
