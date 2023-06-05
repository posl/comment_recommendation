def main():
    a = input().split()
    if a.count(a[0]) == 3 or a.count(a[1]) == 3 or a.count(a[2]) == 3 or a.count(a[3]) == 3 or a.count(a[4]) == 3:
        if a.count(a[0]) == 2 or a.count(a[1]) == 2 or a.count(a[2]) == 2 or a.count(a[3]) == 2 or a.count(a[4]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
