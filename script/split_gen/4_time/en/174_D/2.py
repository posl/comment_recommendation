def main():
    n = int(input())
    s = input()
    print(min(s[:i].count('W') + s[i:].count('R') for i in range(n)))
