def main():
    S = input()
    if S.endswith("er"):
        print("er")
    elif S.endswith("ist"):
        print("ist")
    else:
        print("No er or ist")

if __name__ == '__main__':
    main()