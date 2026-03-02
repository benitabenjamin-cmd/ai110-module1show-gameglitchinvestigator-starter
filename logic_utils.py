def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 100
    # FIXME: User might select invalid difficulty in UI
    # FIX: Copilot + me added ValueError handling to prevent invalid difficulty
    raise ValueError(
        f"Invalid difficulty level: {difficulty}. Choose from 'Easy', 'Normal', or 'Hard'."
    )

def parse_guess(raw: str, low: int, high: int):
    """
    Parse raw input into a guess, returning (is_valid, value, error_message).

    Ensures input is a whole number and within the range [low, high].
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    raw = raw.strip()

    # Check for decimal input
    if "." in raw:
        return False, None, "Decimal numbers are not allowed. Please enter a whole number."

    # Check for valid integer (allow negative numbers)
    if not (raw.isdigit() or (raw.startswith('-') and raw[1:].isdigit())):
        return False, None, "That is not a valid number."

    value = int(raw)

    # Check if within range
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    # FIX: Copilot + me added optional low/high range validation for better input control
    # Example: if value < low or value > high:
    return True, value, None

def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIXME: Original code might crash if types differ
    # FIX: Copilot + me added int conversion and type-safety to prevent crashes
    try:
        guess = int(guess)
        secret = int(secret)
    except Exception:
        return "Error", "Invalid comparison due to type mismatch."

    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📈 Go LOWER!"
    else:
        return "Too Low", "📉 Go HIGHER!"
    
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Copilot + me preserved original scoring logic
    if outcome == "Win":
        points = max(100 - 10 * (attempt_number + 1), 10)
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        # If the attempt number is even, add 5 points; otherwise, subtract 5 points.
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score