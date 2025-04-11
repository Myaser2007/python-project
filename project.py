# checks the length of the password and if it has any lower and upper letters,
def check_the_password(password):
    strength_points = 0
    if len(password) >= 8:
        strength_points = strength_points + 1
    if any(char.islower() for char in password):
        strength_points = strength_points + 1
    if any(char.isupper() for char in password):
        strength_points = strength_points + 1

    # checks if the password contains numbers

    if any(char.isdigit() for char in password):
        strength_points = strength_points + 1

    # calculates the strength points of the password
    if strength_points == 4:
        print("💪 you have a Strong password")
    elif strength_points == 3:
        print("🟡 your password is Medium")
    else:
        print("🔴 your password is Weak")

# asks the user to enter his password
pas = input("Enter Your Password")
check_the_password(pas)
