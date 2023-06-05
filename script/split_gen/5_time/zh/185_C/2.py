def cut_iron_rod(iron_rod_length):
    if iron_rod_length == 12:
        return 1
    elif iron_rod_length == 13:
        return 12
    else:
        if iron_rod_length % 2 == 0:
            return cut_iron_rod(iron_rod_length - 1) + 1
        else:
            return cut_iron_rod(iron_rod_length - 1)
