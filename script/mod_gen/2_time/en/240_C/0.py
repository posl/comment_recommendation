def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print('Yes' if sum(A) <= X and X <= sum(B) else 'No')

if __name__ == '__main__':
    main()