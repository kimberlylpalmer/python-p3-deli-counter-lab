def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        line_status += " ".join(
            [f"{index + 1}. {name}" for index, name in enumerate(katz_deli)]
        )
        print(line_status)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")
