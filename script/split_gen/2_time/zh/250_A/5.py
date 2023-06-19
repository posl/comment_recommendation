def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    if r == 1 and c == 1:
        print(0)
        return
    if r == 1 and c == w:
        print(0)
        return
    if r == h and c == 1:
        print(0)
        return
    if r == h and c == w:
        print(0)
        return
    if r == 1 or r == h:
        print(1)
        return
    if c == 1 or c == w:
        print(1)
        return
    print(2)
