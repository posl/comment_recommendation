def getPluralForm(input):
    if input[-1] == "s":
        return input + "es"
    else:
        return input + "s"

if __name__ == '__main__':
    getPluralForm()