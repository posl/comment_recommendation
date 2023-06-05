def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    if S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')
