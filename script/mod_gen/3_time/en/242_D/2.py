def main():
    S = input()
    Q = int(input())
    T = [0]*Q
    K = [0]*Q
    for i in range(Q):
        T[i], K[i] = map(int, input().split())
    for i in range(Q):
        print(solve(S, T[i], K[i]))

if __name__ == '__main__':
    main()