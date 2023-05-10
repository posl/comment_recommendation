def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))
    ans = 0
    for i in range(1,N):
        if S[i] == '1':
            ans += 1
    ans_ = ans
    if S[0] == '0':
        ans_ += 1
    else:
        ans_ -= 1
    ans__ = ans_
    for i in range(1,N):
        if S[i] == '0':
            ans_ += 1
        else:
            ans_ -= 1
        ans__ = max(ans__,ans_)
    ans = 0
    for i in range(1,N):
        if S[i] == '1':
            ans += 1
    ans_ = ans
    if S[0] == '1':
        ans_ += 1
    else:
        ans_ -= 1
    ans__ = ans_
    for i in range(1,N):
        if S[i] == '1':
            ans_ += 1
        else:
            ans_ -= 1
        ans__ = max(ans__,ans_)
    print(ans__)
