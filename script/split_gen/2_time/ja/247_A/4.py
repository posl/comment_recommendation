def main():
    S = input()
    ans = ''
    for i in range(4):
        if i == 3:
            ans += '0'
        else:
            ans += S[i+1]
    print(ans)
