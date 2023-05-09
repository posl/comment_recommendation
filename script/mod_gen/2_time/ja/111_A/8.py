def main():
    num = input()
    print(num.replace("1", "X").replace("9", "1").replace("X", "9"))

if __name__ == '__main__':
    main()