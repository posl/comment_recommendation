def main():
    a = list(map(int, input().split()))
    a.sort()
    if a.count(a[0]) == 2 and a.count(a[4]) == 3:
        print("Yes")
    elif a.count(a[0]) == 3 and a.count(a[4]) == 2:
        print("Yes")
    else:
        print("No")
