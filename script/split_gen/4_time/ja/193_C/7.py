def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    ans = N
    for i in range(2, int(N**0.5)+1):
        tmp = i
        while tmp <= N:
            tmp *= i
            ans -= 1
    print(ans)
