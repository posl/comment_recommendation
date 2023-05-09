def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        print(S[(k - 1) % len(S)])

if __name__ == '__main__':
    main()