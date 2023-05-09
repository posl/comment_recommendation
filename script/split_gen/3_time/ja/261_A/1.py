def main():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 < l2 or r2 < l1:
        print(0)
    elif r1 == l2:
        print(0)
    elif r2 == l1:
        print(0)
    elif l1 < l2:
        if r1 < r2:
            print(r1 - l2)
        elif r1 == r2:
            print(r1 - l2)
        elif r2 < r1:
            print(r2 - l2)
    elif l2 < l1:
        if r2 < r1:
            print(r2 - l1)
        elif r2 == r1:
            print(r2 - l1)
        elif r1 < r2:
            print(r1 - l1)
