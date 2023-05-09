def main():
    N = int(input())
    S = list(map(int, input().split()))
    a = []
    b = []
    for i in range(N):
        a.append((S[i]+3)/4)
        b.append((S[i]-3)/4)
    if max(a) < min(b):
        print(N)
    elif min(a) > max(b):
        print(0)
    else:
        print(N - (a.index(max(a))+1) - (N - b.index(min(b))))

if __name__ == '__main__':
    main()