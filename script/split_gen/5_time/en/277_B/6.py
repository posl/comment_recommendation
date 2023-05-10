def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("Yes" if len(set(s)) == n else "No")
