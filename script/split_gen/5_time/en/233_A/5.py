def main():
    a = input()
    a = a.split(' ')
    x = int(a[0])
    y = int(a[1])
    if x >= y:
        print(0)
    else:
        print(y-x)
