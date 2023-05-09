def main():
    S = input()
    T = input()
    for i in range(len(T) + 1):
        if S[:i] + S[-len(T) + i:] == T.replace('?', 'a'):
            print('Yes')
        else:
            print('No')
