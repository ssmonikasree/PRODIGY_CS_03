import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Calculate strength score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine strength level
    strength = ""
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Your password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Your password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Your password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Your password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Your password should include at least one special character (e.g., !, @, #, $, etc.).")

    # Construct the result
    result = {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

    return result

def main():
    print("Welcome to the Password Strength Assessment Tool!")
    
    while True:
        password = input("Please enter a password to assess: ")
        result = assess_password_strength(password)
        
        print(f"\nPassword Strength: {result['strength']}")
        print(f"Score: {result['score']} out of 5")
        
        if result['feedback']:
            print("Suggestions to improve your password:")
            for item in result['feedback']:
                print(f"- {item}")
        else:
            print("Your password is strong!")

        continue_choice = input("\nDo you want to assess another password? (yes/no): ").strip().lower()
        if continue_choice not in ['yes', 'y']:
            print("Thank you for using the Password Strength Assessment Tool!")
            break

if __name__ == "__main__":
    main()
