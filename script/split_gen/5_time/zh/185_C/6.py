def cut_iron(L):
    if L == 12:
        return 1
    else:
        return cut_iron(L-1) + (L-1) * cut_iron(L-2)
