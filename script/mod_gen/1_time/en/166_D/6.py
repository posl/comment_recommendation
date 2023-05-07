def main():
    X = int(input())
    i = 0
    while i**5 < X:
        j = 0
        while j**5 < X:
            if i**5 - j**5 == X:
                print(i, -j)
                return
            j += 1
        i += 1

if __name__ == '__main__':
    main()