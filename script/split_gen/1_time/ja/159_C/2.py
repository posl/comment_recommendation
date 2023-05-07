def main():
    L = int(input())
    ans = 0
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            if i * j > L:
                break
            ans = max(ans, i * j * (L - i * j))
    print(ans)
