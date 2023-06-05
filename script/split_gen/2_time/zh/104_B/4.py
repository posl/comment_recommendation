def main():
    S = input()
    if S[0]=='A' and S[2:-1].count('C')==1 and S[1:].islower():
        print('AC')
    else:
        print('WA')
