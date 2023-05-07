def main():
    N = int(input())
    count = 0
    d = {}
    for i in range(N):
        #print(i)
        s = input().split()
        #print(s)
        s = s[1:]
        #print(s)
        s = ' '.join(s)
        #print(s)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(len(d))

if __name__ == '__main__':
    main()