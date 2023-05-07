def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 1
        while a < 1000:
            b = 1
            while b < 1000:
                if 4*a*b+3*a+3*b == S[i]:
                    break
                b += 1
            a += 1
        if a == 1000 and b == 1000:
            count += 1
    print(count)
main()
