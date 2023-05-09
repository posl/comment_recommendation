def main():
    # input
    N = input()
    # compute
    ans = 0
    for i in range(len(N)):
        for j in range(len(N)):
            if i == j:
                continue
            ans = max(ans, int(N[:i+1]) * int(N[i+1:]))
    # output
    print(ans)
