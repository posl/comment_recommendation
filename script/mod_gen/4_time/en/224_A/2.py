def main():
    s = input()
    if s[-2:] == "er":
        print("er")
    elif s[-3:] == "ist":
        print("ist")
    else:
        print("None")

if __name__ == '__main__':
    main()