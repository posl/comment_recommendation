def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(1, N):
        l[i] = l[i-1]
        if S[i-1] == 'A' and S[i] == 'C':
            l[i] += 1
    for i in range(Q):
        left, right = map(int, input().split())
        print(l[right-1] - l[left-1])

if __name__ == '__main__':
    main()