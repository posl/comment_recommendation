def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 >= r2 or r1 <= l2:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))
