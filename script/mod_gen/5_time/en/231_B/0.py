def main():
    n = int(input())
    d={}
    for i in range(n):
        s = input()
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))

if __name__ == '__main__':
    main()