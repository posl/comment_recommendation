def main():
    n, k = map(int, input().split())
    s = input()
    happy = 0
    for i in range(n-1):
        happy += 1 if s[i] == s[i+1] else 0
    print(min(happy + 2*k, n-1))
