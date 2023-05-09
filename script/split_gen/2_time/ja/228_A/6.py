def main():
    s, t, x = map(int, input().split())
    if s <= x < t:
        print("Yes")
    elif s > t and s <= x:
        print("Yes")
    elif s > t and x < t:
        print("Yes")
    else:
        print("No")
