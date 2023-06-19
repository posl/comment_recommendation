def get_ABC_ARC_AGC(R):
    if R < 1200:
        return "ABC"
    elif R < 2800:
        return "ARC"
    else:
        return "AGC"

if __name__ == '__main__':
    get_ABC_ARC_AGC()