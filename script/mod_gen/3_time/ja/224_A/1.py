def main():
    S = input()
    if S[-2:] == "er":
        print("er")
    elif S[-3:] == "ist":
        print("ist")
    else:
        print("er")

if __name__ == '__main__':
    main()