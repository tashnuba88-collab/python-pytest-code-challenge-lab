import pytest
from palindrome import longest_palindromic_substring


class TestLongestPalindromicSubstring:

    def test_babad(self):
        result = longest_palindromic_substring("babad")
        assert result in ("bab", "aba")

    def test_cbbd(self):
        assert longest_palindromic_substring("cbbd") == "bb"

    def test_racecar(self):
        assert longest_palindromic_substring("racecar") == "racecar"

    def test_single_character(self):
        assert longest_palindromic_substring("a") == "a"

    def test_two_different_characters(self):
        result = longest_palindromic_substring("ac")
        assert result in ("a", "c")

    def test_empty_string(self):
        assert longest_palindromic_substring("") == ""

    def test_all_same_character(self):
        assert longest_palindromic_substring("aaaa") == "aaaa"

    def test_no_palindrome_longer_than_one(self):
        result = longest_palindromic_substring("abcde")
        assert len(result) == 1
        assert result in "abcde"

    def test_long_string(self):
        s = "forgeeksskeegfor"
        result = longest_palindromic_substring(s)
        assert result == "geeksskeeg"