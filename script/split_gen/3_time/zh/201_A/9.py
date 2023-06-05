def main():
    a = input().split()
    a.sort()
    if int(a[1])-int(a[0]) == int(a[2])-int(a[1]):
        print("Yes")
    else:
        print("No")
