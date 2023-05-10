def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        else:
            print("Yes")
