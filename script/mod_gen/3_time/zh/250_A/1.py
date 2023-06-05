def problems250_a():
    H,W = map(int, input().split())
    R,C = map(int, input().split())
    print(4 if R in [1,H] and C in [1,W] else 3 if R in [1,H] or C in [1,W] else 2)

if __name__ == '__main__':
    problems250_a()