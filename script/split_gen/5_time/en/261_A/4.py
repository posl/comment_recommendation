def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 < l2:
        if l2 < r1:
            if r1 < r2:
                print(r1 - l2)
            else:
                print(r2 - l2)
        else:
            print(0)
    else:
        if l1 < r2:
            if r2 < r1:
                print(r2 - l1)
            else:
                print(r1 - l1)
        else:
            print(0)
