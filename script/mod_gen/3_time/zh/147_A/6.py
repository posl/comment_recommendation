def main():
    a = input()
    a = a.split(" ")
    a = [int(n) for n in a]
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()