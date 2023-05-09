def main():
    # input
    X, N = map(int, input().split())
    ps = [*map(int, input().split())] if N else []
    # compute
    for i in range(1000):
        if X-i not in ps:
            ans = X-i
            break
        if X+i not in ps:
            ans = X+i
            break
    # output
    print(ans)
