def cut_iron_bar(length):
    if length == 12:
        return 1
    else:
        return length * cut_iron_bar(length - 1)

if __name__ == '__main__':
    cut_iron_bar()