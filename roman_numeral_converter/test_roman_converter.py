import roman_numeral_converter.roman_converter

def test_sending_zero_returns_empty_string():
    assert "" == converter(0)
    