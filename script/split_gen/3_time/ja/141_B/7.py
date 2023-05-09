def main():
    S = input()
    ans = 'Yes'
    for i in range(0,len(S),2):
        if S[i] in 'RL':
            ans = 'No'
            break
    for i in range(1,len(S),2):
        if S[i] in 'UD':
            ans = 'No'
            break
    print(ans)
