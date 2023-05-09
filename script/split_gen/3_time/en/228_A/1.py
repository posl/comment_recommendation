def main():
    s, t, x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    elif t < s and (x < t or s <= x):
        print("Yes")
    else:
        print("No")
