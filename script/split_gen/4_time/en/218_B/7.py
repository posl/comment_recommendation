def main():
    #input
    P = list(map(int, input().split()))
    #compute
    ans = ['a']*26
    for i in range(26):
        ans[P[i]-1] = chr(97+i)
    #output
    print(''.join(ans))
