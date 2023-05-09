def main():
    s,t,x = map(int, input().split())
    if s <= x:
        if x < t:
            print("Yes")
        elif s < t:
            print("No")
        else:
            if x == s:
                print("Yes")
            else:
                print("No")
    else:
        if t < s:
            print("Yes")
        else:
            print("No")
