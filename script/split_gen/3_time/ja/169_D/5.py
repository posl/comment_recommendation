def main():
    N = int(input())
    ans = 0
    i = 2
    while i*i <= N:
        if N%i == 0:
            ans += 1
            N = N//i
        else:
            i += 1
    if N != 1:
        ans += 1
    print(ans)
