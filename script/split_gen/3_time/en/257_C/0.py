def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    children = []
    adults = []
    for i in range(N):
        if S[i] == '0':
            children.append(W[i])
        else:
            adults.append(W[i])
    children.sort()
    adults.sort()
    if len(children) == 0:
        print(0)
        return
    if len(adults) == 0:
        print(len(children))
        return
    ans = 0
    for i in range(len(adults)):
        ans += (adults[i] >= children[i])
    print(ans)
