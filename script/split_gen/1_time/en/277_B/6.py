def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print("Yes" if len(set(s)) == n and all(s[i][0] in "HDCS" and s[i][1] in "A23456789TJQK" for i in range(n)) else "No")
