def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if s < a or (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")
