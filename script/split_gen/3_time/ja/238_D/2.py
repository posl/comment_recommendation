def main():
    t = int(input())
    for i in range(t):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        else:
            if a & (s-a) == 0:
                print("Yes")
            else:
                print("No")
