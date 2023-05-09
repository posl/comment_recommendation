def main():
    a, b = [int(x) for x in input().split()]
    if (str(a)*b) < (str(b)*a):
        print(str(a)*b)
    else:
        print(str(b)*a)
    return
