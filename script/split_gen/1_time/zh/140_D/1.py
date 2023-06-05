def main():
    n, k = map(int, input().split())
    s = input()
    happy = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            happy += 1
    happy += min(n - 1, 2 * k)
    print(happy)
