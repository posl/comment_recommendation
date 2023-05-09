def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif (s - a) % 2 == 0:
            print("Yes")
        else:
            print("No")
