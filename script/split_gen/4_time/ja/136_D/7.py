def main():
    s = input()
    l = len(s)
    rl = [0] * l
    rr = [0] * l
    for i in range(0, l):
        if s[i] == 'R':
            rl[i] += 1
            rr[i - 1] += 1
        else:
            rr[i] += 1
            rl[i + 1] += 1
    ans = []
    for i in range(0, l):
        ans.append(str(rl[i] + rr[i]))
    print(' '.join(ans))
