def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    #print(p)
    index = [0]*n
    for i in range(n):
        index[p[i]] = i
    #print(index)
    #print(n)
    #print(p)
    #print(index)
    #print(p.index(0))
    #print(index[p.index(0)])
    #print(p)
    #prin

if __name__ == '__main__':
    main()