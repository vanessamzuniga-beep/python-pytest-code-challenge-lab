from palindrome import longest_palindromic_substring

# Odd Length Test
def test_odd_length_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

# Even Length Test
def test_even_length_palindrome():
    result = longest_palindromic_substring("cbbd")
    assert result == "bb"

# Entire String Test
def test_entire_string_is_palindrome():
    result = longest_palindromic_substring("racecar")
    assert result == "racecar"

# Single Character Test
def test_single_character():
    result = longest_palindromic_substring("a")
    assert result == "a"

# Test Empty String
def test_empty_string():
    result = longest_palindromic_substring("")
    assert result == ""

# Test long strings
def test_long_string():
    result = longest_palindromic_substring("abaxyzzyxf")
    assert result == "xyzzyx"

# Test No Palindrome
def test_no_palindrome():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1