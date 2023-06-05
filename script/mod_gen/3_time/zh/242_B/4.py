def solve():
    s = input()
    ss = sorted(s)
    if ss[0] == ss[-1]:
        print(ss[0] * len(s))
    else:
        print("".join(ss))

if __name__ == '__main__':
    solve()