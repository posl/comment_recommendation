def cut_iron_bar(length):
    if length == 12:
        return 1
    elif length < 12:
        return 0
    else:
        return cut_iron_bar(length - 1) + cut_iron_bar(length - 2) + cut_iron_bar(length - 3) + cut_iron_bar(length - 4) + cut_iron_bar(length - 5) + cut_iron_bar(length - 6)
