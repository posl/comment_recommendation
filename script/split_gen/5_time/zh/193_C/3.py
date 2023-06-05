def main():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(ans)
