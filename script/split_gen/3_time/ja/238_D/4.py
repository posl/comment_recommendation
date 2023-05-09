def main():
    t = int(input())
    for i in range(t):
        a,s = map(int,input().split())
        if a > s:
            print("No")
            continue
        if a == s:
            print("Yes")
            continue
        if a == 0:
            print("No")
            continue
        if s % 2 == 0:
            if a % 2 == 0:
                print("Yes")
                continue
            else:
                print("No")
                continue
        else:
            if a % 2 == 1:
                print("Yes")
                continue
            else:
                print("No")
                continue
