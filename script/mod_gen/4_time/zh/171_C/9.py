def convert(num):
    num -= 1
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if num < 26:
        return alphabet[num]
    elif num < 26+26**2:
        return alphabet[num//26-1]+alphabet[num%26]
    elif num < 26+26**2+26**3:
        return alphabet[num//26//26-1]+alphabet[num//26%26-1]+alphabet[num%26]
    elif num < 26+26**2+26**3+26**4:
        return alphabet[num//26//26//26-1]+alphabet[num//26//26%26-1]+alphabet[num//26%26-1]+alphabet[num%26]
    elif num < 26+26**2+26**3+26**4+26**5:
        return alphabet[num//26//26//26//26-1]+alphabet[num//26//26//26%26-1]+alphabet[num//26//26%26-1]+alphabet[num//26%26-1]+alphabet[num%26]
    elif num < 26+26**2+26**3+26**4+26**5+26**6:
        return alphabet[num//26//26//26//26//26-1]+alphabet[num//26//26//26//26%26-1]+alphabet[num//26//26//26%26-1]+alphabet[num//26//26%26-1]+alphabet[num//26%26-1]+alphabet[num%26]
    elif num < 26+26**2+26**3+26**4+26**5+26**6+26**7:
        return alphabet[num//26//26//26//26//26//26-1]+alphabet[num//26//26//26//26//26%26-1]+alphabet[num//26//26//26//26%26-1]+alphabet[num//26//26//26%26-1]+alphabet[num//26//26%26-1]+alphabet[num//26%26-1]+alphabet[num%26]
    elif num < 26

if __name__ == '__main__':
    convert()