def main():
    S = input()
    for i in range(len(S)):
        if (i+1)%2==1 and S[i] not in ('R','U','D'):
            print('No')
            return
        elif (i+1)%2==0 and S[i] not in ('L','U','D'):
            print('No')
            return
    print('Yes')
