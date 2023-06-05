def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for i in range(n):
        count += A.count(B[C[i]-1])
    print(count)

if __name__ == '__main__':
    main()