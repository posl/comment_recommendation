def main():
    S = input()
    d = {}
    for i in S:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] == 1:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()