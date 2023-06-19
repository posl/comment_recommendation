def main():
    n,q = map(int, input().split())
    A = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    A.sort()
    for i in range(q):
        num = 0
        for j in range(n):
            if x[i] <= A[j]:
                num += 1
        print(num)

if __name__ == '__main__':
    main()