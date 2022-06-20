"""
Zajęcia Python Luzino
Sławomir Jankowski
"""

import unittest
import string_processing


class TestTrimString(unittest.TestCase):
    def test_trim_string_left(self):
        string_to_test = string_processing.StringProcessing('    To jest tekst testowy.')
        expected_result = 'To jest tekst testowy.'

        string_to_test.trim_string()
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_trim_string_right(self):
        string_to_test = string_processing.StringProcessing('To jest tekst testowy.    ')
        expected_result = 'To jest tekst testowy.'

        string_to_test.trim_string()
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_trim_string_both(self):
        string_to_test = string_processing.StringProcessing('    To jest tekst testowy.    ')
        expected_result = 'To jest tekst testowy.'

        string_to_test.trim_string()
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_trim_string_special_whitespaces(self):
        string_to_test = string_processing.StringProcessing('\t \n \r \f To jest tekst testowy.\u2005 \u2007')
        expected_result = 'To jest tekst testowy.'

        string_to_test.trim_string()
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)


class TestReplaceSubstring(unittest.TestCase):
    def test_replace_substring_space_with_asterisk(self):
        string_to_test = string_processing.StringProcessing('To jest tekst, w którym spacje zostaną zamienione na gwiazdki.')
        expected_result = 'To*jest*tekst,*w*którym*spacje*zostaną*zamienione*na*gwiazdki.'

        string_to_test.replace_substring(' ', '*')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_replace_substring_many_characters(self):
        string_to_test = string_processing.StringProcessing('To jest ciąg znaków, w którym jedna sekwencja znaków zostanie zamieniona na inną sekwencję znaków.')
        expected_result = 'To jest ciąg zębów, w którym jedna sekwencja zębów zostanie zamieniona na inną sekwencję zębów.'

        string_to_test.replace_substring('znaków', 'zębów')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_replace_substring_with_empty_character(self):
        string_to_test = string_processing.StringProcessing('To jest ciąg znaków, w którym pewna sekwencja znaków zostanie usunięta.')
        expected_result = 'To jest ciąg zków, w którym pew sekwencja zków zostanie usunięta.'

        string_to_test.replace_substring('na', '')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)


class TestAddPrefix(unittest.TestCase):
    def test_add_prefix(self):
        string_to_test = string_processing.StringProcessing('To jest tekst, do którego zostanie dodany ciąg znaków na początku.')
        expected_result = '71830To jest tekst, do którego zostanie dodany ciąg znaków na początku.'

        string_to_test.add_prefix('71830')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_add_prefix_existing(self):
        string_to_test = string_processing.StringProcessing('71830To jest tekst, do którego nie zostanie dodany ciąg znaków na początku.')
        expected_result = '71830To jest tekst, do którego nie zostanie dodany ciąg znaków na początku.'

        string_to_test.add_prefix('71830')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)


class TestAddSuffix(unittest.TestCase):
    def test_add_suffix(self):
        string_to_test = string_processing.StringProcessing('To jest tekst, do którego zostanie dodany ciąg znaków na końcu.')
        expected_result = 'To jest tekst, do którego zostanie dodany ciąg znaków na końcu.71830'

        string_to_test.add_suffix('71830')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)

    def test_add_suffix_existing(self):
        string_to_test = string_processing.StringProcessing('To jest tekst, do którego nie zostanie dodany ciąg znaków na końcu.71830')
        expected_result = 'To jest tekst, do którego nie zostanie dodany ciąg znaków na końcu.71830'

        string_to_test.add_suffix('71830')
        self.assertEqual(string_to_test.get_current_processing_result(), expected_result)


if __name__ == '__main__':
    unittest.main()
