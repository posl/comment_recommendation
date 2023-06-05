def main():
    n = int(input())
    a = [input() for i in range(n)]
    print("Yes" if a.count("For") > n//2 else "No")
