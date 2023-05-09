def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 and r1 >= l2:
        print(max(r1, r2) - l2)
    elif l1 <= r2 and r1 >= r2:
        print(r2 - min(l1, l2))
    else:
        print(0)
