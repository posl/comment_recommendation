def main():
    v, t, s, d = [int(i) for i in input().split()]
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")
