def main():
    l, q = map(int, input().split())
    cuts = [0,l]
    for _ in range(q):
        c,x = map(int, input().split())
        if c == 1:
            cuts.append(x)
            cuts.sort()
        else:
            left = cuts[bisect.bisect_left(cuts, x)-1]
            right = cuts[bisect.bisect_right(cuts, x)]
            print(right-left)
    return
