# checks the length of the password and if it has any lower and upper letters,
def check_password(password):
    strength = 0
    if len(password) >= 8:
        strength = strength + 1
    if any(char.islower() for char in password):
        strength = strength + 1
    if any(char.isupper() for char in password):
        strength = strength + 1

    # checks if the password contains numbers

    if any(char.isdigit() for char in password):
        strength = strength + 1

    # calculates the strength points of the password
    if strength == 4:
        print("💪 you have a Strong password")
    elif strength == 3:
        print("🟡 your password is Medium")
    else:
        print("🔴 your password is Weak")

# asks the user to enter his password
pas = input("Enter Your Password")
check_password(pas)
