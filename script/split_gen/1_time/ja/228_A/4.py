def main():
    s, t, x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    elif s > t and x < t:
        print("Yes")
    elif s > t and s <= x:
        print("Yes")
    else:
        print("No")
