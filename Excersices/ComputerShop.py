options = {
    "1":"keyboard",
    "2":"monitor",
    "3":"mouse",
    "4":"harddrive",
    "5":"cable",
    "6":"headphone"
}

chosen_value = None

while chosen_value != "-":
    if chosen_value in options:
        print(f""{options[chosen_value]})
    chosen_value = input(">")
