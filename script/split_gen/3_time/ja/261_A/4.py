def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 and l2 < r1:
        print(min(r1, r2) - l2)
    elif l2 <= l1 and l1 < r2:
        print(min(r1, r2) - l1)
    else:
        print(0)
