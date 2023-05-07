def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    gen = 0
    for i in range(N, 0, -1):
        if P[i] == 1:
            gen += 1
            break
        gen += 1
    print(gen)

if __name__ == '__main__':
    main()