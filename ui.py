

def square_box(title, options):
    width = 34

    def print_line(text):
        print("| " + text.ljust(width - 2) + " |")

    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("+" + "-" * width + "+")



    for option in options:
        print("| " + option.ljust(width - 2) + " |")
        print("+" + "-" * width + "+")


    if not options:
        print("data not found")


    elif isinstance(title, dict):
        for username, password in options.items():
            print_line("Username: " + username)
            print_line("Password: " + password)
            print_line("-" * (width - 2))

    else:
        for content in options:
            print_line(content)




    print("+" + "-" * width + "+")





