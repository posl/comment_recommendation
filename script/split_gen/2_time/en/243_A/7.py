def main():
    v,a,b,c = [int(x) for x in input().split()]
    if v%a == 0:
        print("F")
    elif v%b == 0:
        print("M")
    elif v%c == 0:
        print("T")
    else:
        print("M")
