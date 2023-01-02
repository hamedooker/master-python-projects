computer_parts = {
    "1":"keyboard",
    "2":"monitor",
    "3":"mouse",
    "4":"harddrive",
    "5":"cable",
    "6":"headphone"
}

chosen_value = None
while chosen_value != "-":
    if chosen_value in computer_parts:
        chosen_part = computer_parts[chosen_value]
        print(f"Adding {chosen_part}")
    else:
        for key, value in computer_parts.items():
            print(f"{key}: {value}")

    chosen_value = input(">")
