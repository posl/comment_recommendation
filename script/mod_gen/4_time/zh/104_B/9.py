def main():
    input_str = input()
    if input_str[0] != "A":
        print("WA")
        return
    if input_str[2:-1].count("C") != 1:
        print("WA")
        return
    for i in range(len(input_str)):
        if i == 0 or i == 2 or i == len(input_str) - 1:
            continue
        if input_str[i].isupper():
            print("WA")
            return
    print("AC")

if __name__ == '__main__':
    main()