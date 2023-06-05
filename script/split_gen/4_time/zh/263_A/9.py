def main():
    a = input()
    a = a.split()
    if a[0] == a[1] and a[1] == a[2]:
        if a[3] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[1] and a[1] == a[3]:
        if a[2] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[1] and a[1] == a[4]:
        if a[2] == a[3]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[2] and a[2] == a[3]:
        if a[1] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[2] and a[2] == a[4]:
        if a[1] == a[3]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[3] and a[3] == a[4]:
        if a[1] == a[2]:
            print("Yes")
        else:
            print("No")
    elif a[1] == a[2] and a[2] == a[3]:
        if a[0] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[1] == a[2] and a[2] == a[4]:
        if a[0] == a[3]:
            print("Yes")
        else:
            print("No")
    elif a[1] == a[3] and a[3] == a[4]:
        if a[0] == a[2]:
            print("Yes")
        else:
            print("No")
    elif a[2] == a[3] and a[3] == a[4]:
        if a[0] == a[1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
