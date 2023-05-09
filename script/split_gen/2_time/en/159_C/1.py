def main():
    L = int(input())
    ans = 0
    for i in range(1, L):
        for j in range(1, L):
            k = L - i - j
            if k < 1:
                break
            ans = max(ans, i * j * k)
    print(ans)
