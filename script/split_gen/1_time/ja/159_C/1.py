def main():
    L = int(input())
    ans = 0
    for i in range(1, L):
        for j in range(1, L):
            for k in range(1, L):
                if i + j + k == L:
                    ans = max(ans, i * j * k)
    print(ans)
