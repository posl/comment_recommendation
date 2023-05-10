def main():
    # input
    N, T = map(int, input().split())
    As = list(map(int, input().split()))
    # compute
    time = 0
    for i in range(N):
        time += As[i]
        if time >= T:
            ans1 = i+1
            ans2 = T - (time - As[i])
            break
    # output
    print(ans1, ans2)
