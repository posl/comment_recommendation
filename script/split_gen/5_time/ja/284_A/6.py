def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        print(s[n-1-i])
