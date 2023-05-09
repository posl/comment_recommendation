def main():
    s,t,x = map(int,input().split())
    if s < t:
        if s <= x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if 0 <= x <= t:
            print("Yes")
        elif s <= x <= 23:
            print("Yes")
        else:
            print("No")
