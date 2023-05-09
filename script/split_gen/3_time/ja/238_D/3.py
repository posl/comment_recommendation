def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if s < a:
            print("No")
        elif (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")
