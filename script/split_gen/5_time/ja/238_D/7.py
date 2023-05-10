def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if a == 0 and s == 0:
            print("Yes")
            continue
        if a == 0:
            print("No")
            continue
        if a & 1 == 1 and s & 1 == 0:
            print("No")
            continue
        if a & 1 == 0 and s & 1 == 1:
            print("No")
            continue
        if a & 1 == 1 and s & 1 == 1:
            print("Yes")
            continue
        if a & 1 == 0 and s & 1 == 0:
            print("Yes")
            continue
