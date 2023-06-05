def main():
    N = int(input())
    S = input()
    if N % 2 != 0:
        print('error')
        return
    for i in range(0, N, 2):
        if S[i] == '"':
            if S[i + 1] == '"':
                print('error')
                return
            else:
                S = S[:i] + '.' + S[i + 1:]
    print(S)
