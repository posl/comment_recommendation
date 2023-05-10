def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if s % 2 == 0:
            if a % 2 == 0:
                print("Yes")
            else:
                print("No")
        else:
            if a % 2 == 1:
                print("Yes")
            else:
                print("No")
