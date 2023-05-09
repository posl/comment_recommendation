def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1 and r2 >= l1:
        print(max(l2, l1) - min(r1, r2))
    else:
        print(0)
