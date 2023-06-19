def main():
    n = input()
    if n[-1] in "24579":
        print("hon")
    elif n[-1] in "0168":
        print("pon")
    else:
        print("bon")

if __name__ == '__main__':
    main()