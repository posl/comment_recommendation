def main():
    # S = input()
    S = '10888869450418352160768000001'
    # S = '1355506027'
    # S = '40004'
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += 1
        else:
            if S[i] == '0':
                ans += 1
            else:
                ans += 2
    print(ans)
