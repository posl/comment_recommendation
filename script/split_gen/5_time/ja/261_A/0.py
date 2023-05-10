def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1 and l1 <= r2:
        print(max(0, min(r1, r2) - max(l1, l2)))
    else:
        print(0)
