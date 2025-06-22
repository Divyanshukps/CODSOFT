import random
import string
import secrets

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a secure random password with specified complexity"""
    character_set = ""
    
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation
    
    if not character_set:
        print("Error: No character types selected!")
        return None
    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_special:
        password.append(secrets.choice(string.punctuation))
    
    remaining_length = length - len(password)
    password.extend(secrets.choice(character_set) for _ in range(remaining_length))
    
    random.shuffle(password)
    
    return ''.join(password)

def get_yes_no_input(prompt):
    """Helper function for yes/no inputs"""
    while True:
        response = input(prompt).lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'")

def main():
    print("\n=== Secure Password Generator ===")
    
    # Get password length
    while True:
        try:
            length = int(input("\nEnter password length (8-64): "))
            if 8 <= length <= 64:
                break
            print("Please enter a value between 8 and 64")
        except ValueError:
            print("Please enter a valid number")
    
  
    print("\nSelect character types to include:")
    use_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
    use_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no_input("Include digits? (y/n): ")
    use_special = get_yes_no_input("Include special characters? (y/n): ")
    
    # Generate and display password
    password = generate_password(
        length=length,
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_special=use_special
    )
    
    if password:
        print("\nGenerated Password:")
        print("-" * 30)
        print(password)
        print("-" * 30)
        print("\nNote: Please store this password securely!")

if __name__ == "__main__":
    main()
