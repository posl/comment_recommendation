def main():
    T = int(input())
    for i in range(T):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        else:
            if (s-a)%2 == 0:
                print("Yes")
            else:
                print("No")
