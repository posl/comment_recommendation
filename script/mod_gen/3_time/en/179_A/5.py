def pluralForm(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"
print(pluralForm(input()))

if __name__ == '__main__':
    pluralForm()