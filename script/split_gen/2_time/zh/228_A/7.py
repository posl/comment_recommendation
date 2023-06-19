def main():
    s, t, x = [int(i) for i in input().split()]
    if s < t:
        if s <= x and x <= t:
            print("Yes")
        else:
            print("No")
    else:
        if x <= t or s <= x:
            print("Yes")
        else:
            print("No")
