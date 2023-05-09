def main():
    n = input()
    new_n = ""
    for i in n:
        if i == "9":
            new_n += "1"
        else:
            new_n += "9"
    print(new_n)
main()
