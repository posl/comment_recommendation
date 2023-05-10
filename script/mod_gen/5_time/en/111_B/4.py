def main():
    n = int(input())
    while True:
        if len(set(list(str(n)))) == 1:
            print(n)
            break
        n += 1

if __name__ == '__main__':
    main()