def main():
    s, t, x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    else:
        print("No")
