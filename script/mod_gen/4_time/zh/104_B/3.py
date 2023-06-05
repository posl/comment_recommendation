def main():
    input_string = input()
    #print(input_string)
    if input_string[0] == "A":
        if input_string[2:-1].count("C") == 1:
            if input_string[2:-1].islower():
                if input_string[-1].islower():
                    print("AC")
                    return
    print("WA")

if __name__ == '__main__':
    main()