def main():
    s = input()
    if s.endswith("er"):
        print("er")
    elif s.endswith("ist"):
        print("ist")
    else:
        print("error")

if __name__ == '__main__':
    main()