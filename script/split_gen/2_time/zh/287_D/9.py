def main():
    S = input()
    T = input()
    for i in range(len(S) - len(T) + 1):
        if S[i:i + len(T)].replace('?', 'a') >= T.replace('?', 'a'):
            print('Yes')
        else:
            print('No')
