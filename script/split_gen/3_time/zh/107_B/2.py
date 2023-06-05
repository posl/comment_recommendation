def main():
    h, w = map(int, input().split())
    a = [list(input()) for i in range(h)]
    a = [list(i) for i in zip(*a) if i.count(".") != h]
    a = [list(i) for i in zip(*a) if i.count(".") != w]
    for i in a:
        print("".join(i))
