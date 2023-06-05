def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if a <= s:
            print("Yes")
        else:
            print("No")
