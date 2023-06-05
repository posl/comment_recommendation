def main():
    t = int(input())
    for i in range(t):
        a,s = map(int, input().split())
        if a <= s and s%2 == a%2:
            print("Yes")
        else:
            print("No")
