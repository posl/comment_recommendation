def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    a = [i for i in a if "#" in i]
    a = [list(i) for i in zip(*a)]
    a = [i for i in a if "#" in i]
    a = [list(i) for i in zip(*a)]
    for i in a:
        print("".join(i))
