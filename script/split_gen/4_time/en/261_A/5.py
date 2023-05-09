def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1:
        print(max(r1, r2) - l2)
    elif l1 <= r2:
        print(max(r1, r2) - l1)
    else:
        print(0)
