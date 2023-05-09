def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    if N == 2:
        print((v[0]+v[1])/2)
    else:
        for i in range(N-1):
            v[i+1] = (v[i]+v[i+1])/2
        print(v[N-1])

if __name__ == '__main__':
    main()