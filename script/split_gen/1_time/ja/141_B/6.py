def main():
    S = input()
    for i in range(len(S)):
        if i%2==0:
            if S[i] in ['L']:
                print('No')
                exit()
        else:
            if S[i] in ['R']:
                print('No')
                exit()
    print('Yes')
