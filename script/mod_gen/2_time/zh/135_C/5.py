def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N, p)
    #print(p.index(1))
    #print(p.index(N))
    if p.index(1) < p.index(N):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()