def main():
    r, x, y = map(int, input().split())
    if x % r == 0 and y % r == 0:
        print(abs(x//r) + abs(y//r))
    else:
        print(abs(x//r) + abs(y//r) + 1)
