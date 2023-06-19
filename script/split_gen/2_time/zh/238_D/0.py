def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if (s - a) % 2 == 0 and s >= a:
            print("Yes")
        else:
            print("No")
