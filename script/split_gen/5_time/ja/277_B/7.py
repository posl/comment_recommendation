def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print("Yes" if n == len(s) else "No")
