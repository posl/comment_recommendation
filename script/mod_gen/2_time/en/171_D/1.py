def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sum = 0
    for a in A:
        sum += a
    #print(sum)
    for i in range(Q):
        count = 0
        for a in A:
            if a == B[i]:
                count += 1
        sum += (C[i] - B[i]) * count
        print(sum)

if __name__ == '__main__':
    main()