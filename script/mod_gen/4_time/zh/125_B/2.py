def main():
    N = int(input())
    Vs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))
    maxvalue = 0
    for i in range(N):
        if Vs[i] - Cs[i] > 0:
            maxvalue += Vs[i] - Cs[i]
    print(maxvalue)
    return

if __name__ == '__main__':
    main()