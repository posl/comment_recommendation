def main():
    S = input()
    if S[0].islower():
        for i in range(1,len(S),2):
            if not S[i].islower():
                print('No')
                return
        for i in range(0,len(S),2):
            if not S[i].isupper():
                print('No')
                return
        print('Yes')
    else:
        for i in range(1,len(S),2):
            if not S[i].isupper():
                print('No')
                return
        for i in range(0,len(S),2):
            if not S[i].islower():
                print('No')
                return
        print('Yes')
