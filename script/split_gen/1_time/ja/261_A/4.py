def main():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 <= l2:
        print(0)
    elif r1 <= r2:
        print(r1 - l2)
    elif r2 <= l1:
        print(0)
    elif r2 <= r1:
        print(r2 - l1)
    else:
        print(r1 - l1)
