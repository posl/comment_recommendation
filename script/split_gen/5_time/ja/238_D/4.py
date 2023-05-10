def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        x = s - a
        if a & x:
            print("No")
        else:
            print("Yes")
