def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if s - a < a:
            print("No")
            continue
        if s % 2 == 0:
            print("Yes")
        else:
            print("No")
