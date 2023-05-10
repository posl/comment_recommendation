def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(sum(B)-sum(A)+N)

if __name__ == '__main__':
    main()