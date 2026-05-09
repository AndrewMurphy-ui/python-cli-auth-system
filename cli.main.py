from storage import load_cli
from auth import register_user, login_user, show_users


def square_box(title, options):
    width = 34

    print("+" + "-" * width + "+")
    print("|" + title.centre(width) + "|")
    print("+" + "-" * width + "+")



    for option in options:
        print("| " + option.ljust(width - 2) + " |")
        print("+" + "-" * width + "+")





def menu_home() -> None:
    """displays main menu and handles user navigation"""
    users = load_cli()

    if users is None:
        return

    while True:
        square_box("Main Menu", [
            "1. Register a new user",
            "2. Login",
            "3. Show users",
            "exit. Logout"
        ])

        option = input("Type to choose: ").lower().strip()

        if option == "":
            print("error, cannot be blank, please try again")
            continue

        elif option == "1":
            print("menu: signup selected")
            register_user(users)

        elif option == "2":
            print("menu: login selected")
            login_user(users)

        elif option == "3":
            print("menu: show users selected")
            show_users(users)

        elif option == "exit":
            break

        else:
            print("error, try again")





if __name__ == "__main__":
    menu_home()

