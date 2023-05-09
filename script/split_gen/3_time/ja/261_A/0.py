def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 <= r1 <= r2 or l2 <= l1 <= r2 <= r1:
        print(r1 - l2)
    elif l1 <= l2 <= r2 <= r1 or l2 <= l1 <= r1 <= r2:
        print(r2 - l2)
    else:
        print(0)
