def main():
    N, M = map(int, raw_input().split())
    AB = []
    for i in range(N):
        AB.append(map(int, raw_input().split()))
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
    print ans

if __name__ == '__main__':
    main()