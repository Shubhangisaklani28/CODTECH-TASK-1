Name: Shubhangi Saklani   

Company: CODTECH IT SOLUTIONS
ID: CT6WDS212

Domain: Cyber Security and Ethical Hacking

Duration: May to July 2024

Mentor:

**Overview of the project**

#### Purpose
The script is designed to help users evaluate the strength of their passwords and provide feedback on how to improve them. It assesses passwords based on various criteria, such as length, complexity, and uniqueness, and offers detailed feedback for enhancing password security.

#### How It Works
1. **User Input**: The script prompts the user to enter a password for assessment.
2. **Strength Evaluation**: The script evaluates the password based on the following criteria:
   - **Length**: Ensures the password is at least 8 characters long.
   - **Uppercase Letters**: Checks for the presence of at least one uppercase letter.
   - **Lowercase Letters**: Checks for the presence of at least one lowercase letter.
   - **Digits**: Checks for the presence of at least one digit.
   - **Special Characters**: Checks for the presence of at least one special character.
   - **Common Patterns**: Identifies common patterns or sequences that reduce password strength.
   - **Repeated Characters**: Checks for excessive repetition of characters.
   - **Uniqueness (Entropy)**: Assesses the number of unique characters in the password.
3. **Scoring**: The script assigns a score from 0 to 5 based on how well the password meets the criteria.
4. **Feedback**: Detailed feedback is provided to the user on how to improve their password, based on the criteria that were not met.
5. **Output**: The script outputs the strength of the password (Very Weak, Weak, Moderate, Strong, Very Strong) and the score out of 5.

#### Features
- **Length Check**: Ensures the password is sufficiently long.
- **Character Type Checks**: Verifies the presence of uppercase letters, lowercase letters, digits, and special characters.
- **Pattern Recognition**: Identifies and penalizes common patterns and sequences.
- **Repetition Check**: Reduces the score for excessive repetition of characters.
- **Entropy Assessment**: Encourages the use of a diverse set of characters.
- **Detailed Feedback**: Provides specific advice on how to strengthen the password.

#### Usage
1. Run the script in a terminal or command prompt.
2. Enter a password when prompted to receive an assessment of its strength.
3. To exit the script, type `exit`.

#### Example Usage
```sh
$ python password_assessor.py
Enter a password to assess (or type 'exit' to quit): Password123!
Password strength: Strong (Score: 4/5)
  - Your password is strong, but could be improved with more unique characters.
```

#### Benefits
- **User Guidance**: Helps users understand the weaknesses in their passwords and how to address them.
- **Security Enhancement**: Encourages the creation of stronger, more secure passwords.
- **Ease of Use**: Simple command-line interface with clear feedback.

This script is ideal for anyone looking to improve their password security by understanding and addressing the factors that contribute to password strength.
