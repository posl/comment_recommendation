def main():
    N = int(input())
    ans = N - 1
    for i in range(2, N):
        if i*i > N:
            break
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(ans)
