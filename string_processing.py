"""
Zajęcia Python Luzino
Sławomir Jankowski
"""


class StringProcessing:
    """
    Klasa przetwarzająca ciąg znaków otrzymany przy inicjacji.
    """

    _string = ''
    """
    Prywatne pole, w którym przetrzymywana jest aktualna wartość przetwarzanego ciągu znaków.
    """

    # zadanie nr 1
    def __init__(self):
        """
        Inicjuje obiekt przetwarzający ciągi znaków.

        :param string: ciąg znaków do przetwarzania
        """
        pass

    # zadanie nr 2
    def get_current_processing_result(self):
        """
        Zwraca aktualną wartość przetwarzanego ciągu znaków.

        :return: _string
        """
        pass

    # zadanie nr 3
    def trim_string(self):
        """
        Usuwa tzw. białe znaki z początku i z końca przetwarzanego ciągu znaków.
        """
        pass

    # zadanie nr 4
    def replace_substring(self):
        """
        Zastępuje dowolny ciąg znaków wewnątrz przetwarzanego ciągu znaków dowolnym ciągkiem znaków.

        :param what: ciąg znaków, który zostanie zastąpiony
        :param to: ciąg znaków, który zastąpi poprzednią sekwencję
        """
        pass

    # zadanie nr 5
    def add_prefix(self):
        """
        Dodaje przedrostek na początku przetwarzanego ciągu znaków, o ile ten przedrostek nie rozpoczyna słowa.

        :param prefix: przedrostek do dodania
        """
        pass

    #zadanie nr 6
    def add_suffix(self):
        """
        Dodaje przyrostek na końcu przetwarzanego ciągu znaków, o ile ten przyrostek nie kończy słowa.

        :param suffix: przyrostek do dodania
        """
        pass


if __name__ == '__main__':
    pass
