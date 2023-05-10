def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    s = sum(A)
    for b, c in BC:
        s += (c - b) * A.count(b)
        print(s)
        A = [c if a == b else a for a in A]

if __name__ == '__main__':
    main()