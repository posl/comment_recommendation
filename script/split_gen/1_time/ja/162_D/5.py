def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                    if j - i != k - j:
                        cnt += 1
    print(cnt)
