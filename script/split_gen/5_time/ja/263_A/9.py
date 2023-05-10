def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print("No")
    elif a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print("No")
    else:
        print("Yes")
