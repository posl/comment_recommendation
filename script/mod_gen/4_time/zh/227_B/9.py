def main():
    N = int(input())
    S = input().split()
    count = 0
    for i in range(N):
        S[i] = int(S[i])
        a = 1
        b = 1
        while True:
            if 4*a*b+3*a+3*b == S[i]:
                break
            elif 4*a*b+3*a+3*b > S[i]:
                b = 1
                a += 1
            else:
                b += 1
        if a == 1 and b == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    main()