from storage import load_cli
from auth import register_user, login_user, show_users


def menu_home() -> None:
    """displays main menu and handles user navigation"""
    users = load_cli()

    if users is None:
        return

    while True:
        print()
        print("Main Menu")
        print("-" * 30)
        print("type to choose your option")
        print("press 1: register a new user")
        print("press 2: login")
        print("press 3: show users")
        print("press: 'exit' logout")

        option = input("type to choose: ").lower().strip()

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

