def main():
    L = int(input())
    ans = 0
    for a in range(1, L):
        for b in range(1, L):
            if a + b >= L:
                break
            c = L - a - b
            ans = max(ans, a * b * c)
    print(ans)
