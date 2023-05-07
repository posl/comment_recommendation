def main():
    S = input()
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] in ['L','D']:
                print('No')
                return
        else:
            if S[i] in ['R','D']:
                print('No')
                return
    print('Yes')
    return
