def main():
    n = int(input())
    while True:
        if len(set(str(n))) == 1:
            print(n)
            return
        else:
            n += 1

if __name__ == '__main__':
    main()