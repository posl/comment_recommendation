def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    #print(N)
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    #print(d)
    max = 0
    for k in d:
        if d[k] > max:
            max = d[k]
    #print(max)
    for k in sorted(d):
        if d[k] == max:
            print(k)

if __name__ == '__main__':
    main()