def main():
    s = input()
    s = s[::-1].replace("6", "9").replace("9", "6")
    print(s)
main()

if __name__ == '__main__':
    main()