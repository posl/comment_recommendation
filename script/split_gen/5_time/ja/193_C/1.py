def main():
    N = int(input())
    # N = 100000
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        # print(i)
        j = 2
        while i ** j <= N:
            ans -= 1
            j += 1
    print(ans)
