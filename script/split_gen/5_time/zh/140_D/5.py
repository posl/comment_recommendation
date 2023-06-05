def main():
    n, k = map(int, input().split())
    s = input()
    happy = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            happy += 1
    print(min(happy + 2 * k, n-1))
