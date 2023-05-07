def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("Yes" if s.count("For") > s.count("Against") else "No")
