"""
Zajęcia Python Luzino
Sławomir Jankowski
"""

import string_processing


# zadanie nr 7
def main():
    string_to_process = string_processing.StringProcessing('\t\t\t  \riiiiiiiXXXX To jest ciąg znaków do przetworzenia w kilku krokach.XXXZZZ\n\n    ')

    # Tutaj umieść kroki przetwarzające ciąg znaków, by otrzymać poniższy wynik (instrukcja warunkowa)

    if string_to_process.get_current_processing_result() == 'Otóż tak. To jest ciąg znaków do przetworzenia w kilku krokach. Już po zmianach.':
        print('Sukces')
    else:
        print('Porażka')


if __name__ == '__main__':
    main()
