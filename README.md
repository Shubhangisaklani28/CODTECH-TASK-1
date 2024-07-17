# password_checker
This Python script evaluates password strength based on length, complexity, and uniqueness. It checks for the inclusion of uppercase and lowercase letters, digits, special characters, and common patterns. Detailed feedback is provided to help users create more secure passwords. Ideal for enhancing password security. 


### Script Specification

#### Name
Password Strength Assessor

#### Description
This Python script evaluates the strength of passwords based on length, complexity, and uniqueness. It provides detailed feedback to help users create more secure passwords by analyzing various factors, including the inclusion of uppercase and lowercase letters, digits, special characters, and common patterns.

#### Features
1. **Length Check**: Ensures the password is at least 8 characters long.
2. **Uppercase Letter Check**: Verifies that the password contains at least one uppercase letter.
3. **Lowercase Letter Check**: Verifies that the password contains at least one lowercase letter.
4. **Digit Check**: Verifies that the password contains at least one digit.
5. **Special Character Check**: Verifies that the password contains at least one special character (non-alphanumeric).
6. **Common Pattern Check**: Reduces the score if the password contains common patterns or sequences like "12345", "password", etc.
7. **Repeated Characters Check**: Reduces the score if the password contains too many repeated characters.
8. **Uniqueness Check (Entropy)**: Ensures the password has a sufficient number of unique characters.
9. **Detailed Feedback**: Provides feedback on how to improve the password's strength.

#### Usage
1. Save the script to a file, e.g., `password_assessor.py`.
2. Run the script in a terminal or command prompt.
3. Enter a password to assess its strength.
4. The script will display the strength of the password, a score out of 5, and feedback on how to improve the password.
5. To exit the script, type `exit`.

#### Example
```sh
python password_assessor.py
Enter a password to assess (or type 'exit' to quit): Password123!
Password strength: Strong (Score: 4/5)
  - Your password is strong, but could be improved with more unique characters.
```

#### Dependencies
- Python 3.x
- `re` module (standard library)
- `collections` module (standard library)

#### How to Run
1. Save the script to a file, e.g., `password_assessor.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Execute the script by running `python password_assessor.py`.

This script is useful for users who want to enhance their password security by receiving detailed feedback on the strength and composition of their passwords.
