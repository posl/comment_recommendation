def cut_iron_rod(length):
    if length <= 4:
        return 1
    else:
        return cut_iron_rod(length - 1) + cut_iron_rod(length - 4)
