def main():
    n = int(input())
    ps = []
    for i in range(n):
        x, y = map(int, input().split())
        ps.append((x, y))
    s = input()
    if s.count("L") == 0 or s.count("R") == 0:
        print("No")
        return
    l = s.index("L")
    r = s.index("R")
    if l < r:
        print("Yes")
    else:
        print("No")
