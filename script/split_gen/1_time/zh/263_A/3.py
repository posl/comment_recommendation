def main():
    a = input().split()
    a.sort()
    if a[0] == a[1] and a[2] == a[4] or a[0] == a[2] and a[3] == a[4]:
        print("Yes")
    else:
        print("No")
