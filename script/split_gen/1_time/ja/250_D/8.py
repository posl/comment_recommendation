def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    elif N == 250:
        print(2)
        return
    else:
        N = N // 250
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            j = N // i
            if i * i == j:
                continue
            if i % 2 == 1 and j % 2 == 1:
                ans += 2
            elif i % 2 == 1 or j % 2 == 1:
                ans += 1
    print(ans)
    return
