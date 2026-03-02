from logic_utils import check_guess, parse_guess, get_range_for_difficulty

# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     result = check_guess(50, 50)
#     assert result == "Win"
#     assert "Correct" in message

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     result = check_guess(60, 50)
#     assert result == "Too High"
#     assert "LOWER" in message

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     result = check_guess(40, 50)
#     assert result == "Too Low"
#     assert "HIGHER" in message

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_parse_guess_valid():
    ok, val, err = parse_guess("42", 1, 100)
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_guess_empty():
    ok, val, err = parse_guess("", 1, 100)
    assert ok is False
    assert val is None
    assert "Enter a guess" in err

def test_parse_guess_decimal():
    ok, val, err = parse_guess("3.14", 1, 100)
    assert ok is False
    assert val is None
    assert "Decimal" in err

def test_parse_guess_non_number():
    ok, val, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert val is None
    assert "number" in err