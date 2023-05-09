def main():
    a = input()
    a = a.split()
    a1 = int(a[0])
    a2 = int(a[1])
    a3 = int(a[2])
    if a1+a2+a3 >= 22:
        print("bust")
    else:
        print("win")
