"""
    Napisz funkcje sprawdzajaca czy napis podany jako argument do niej
    jest palindromem. Palindrom to napis, ktory czytany od lewej
    do prawej brzmi tak samo jak czytany od prawej do lewej, np kajak.
    Dla ulatwienia zaloz, ze napis bedzie zawsze jednym slowem.
    Zakladamy, ze pusty string jest palindromem.
"""


def check_if_palindrome(string):
    """Sprawdza czy podany string (jedno slowo) jest palindromem.

    :param string: napis do sprawdzenia.
    :return: True jezeli napis jest palindromem,
             False w przeciwnym wypadku.

    """
    l = len(string)
    for i in range(int(l/2):
        if string[i] != string[l-1-i]:
            return False
    return True 
