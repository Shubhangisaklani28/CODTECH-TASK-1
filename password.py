import re
from collections import Counter

def password_strength(password):
    feedback = []
    score = 0

    # Length criteria
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase criteria
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Lowercase criteria
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Digit criteria
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Special character criteria
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Common pattern check
    common_patterns = ["12345", "password", "admin", "qwerty", "letmein"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Password contains common patterns (e.g., '12345', 'password'). Avoid using common patterns.")
        score = max(0, score - 1)

    # Repeated characters check
    char_count = Counter(password.lower())
    most_common_char, count = char_count.most_common(1)[0]
    if count > len(password) // 2:
        feedback.append(f"Password contains too many repetitions of the character '{most_common_char}'.")
        score = max(0, score - 1)

    # Uniqueness check (Entropy)
    unique_chars = len(set(password))
    if unique_chars < len(password) / 2:
        feedback.append("Password should have more unique characters.")
        score = max(0, score - 1)

    # Generate strength description
    if score == 5:
        strength = "Very Strong"
        feedback.append("Your password is very strong.")
    elif score == 4:
        strength = "Strong"
        feedback.append("Your password is strong, but could be improved with more unique characters.")
    elif score == 3:
        strength = "Moderate"
        feedback.append("Your password is moderate. Consider adding more unique characters and varying character types.")
    elif score == 2:
        strength = "Weak"
        feedback.append("Your password is weak. Consider increasing its length and complexity.")
    else:
        strength = "Very Weak"
        feedback.append("Your password is very weak. Consider increasing its length, complexity, and uniqueness.")

    return strength, score, feedback

def main():
    while True:
        password = input("Enter a password to assess (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        strength, score, feedback = password_strength(password)
        print(f"Password strength: {strength} (Score: {score}/5)")
        for comment in feedback:
            print(f"  - {comment}")
        print()

if __name__ == "__main__":
    main()
