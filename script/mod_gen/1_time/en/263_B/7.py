def main():
    N = int(input())
    P = [int(n) for n in input().split()]
    P.insert(0, 0)
    max = 0
    for i in range(N, 1, -1):
        count = 0
        while i > 1:
            i = P[i]
            count += 1
        if count > max:
            max = count
    print(max)

if __name__ == '__main__':
    main()