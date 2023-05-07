def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    C_count = 0
    for i in range(2, len(S) - 1):
        if S[i] == 'C':
            C_count += 1
    if C_count != 1:
        print('WA')
        return
    for i in range(1, len(S)):
        if i == 1 or i == len(S) - 1:
            if S[i] == 'C':
                print('WA')
                return
        else:
            if S[i].isupper():
                print('WA')
                return
    print('AC')
