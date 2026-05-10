

def square_box(title, options):
    width = 34

    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("+" + "-" * width + "+")



    for option in options:
        print("| " + option.ljust(width - 2) + " |")
        print("+" + "-" * width + "+")