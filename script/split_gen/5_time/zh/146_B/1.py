def main():
    N = int(input())
    S = input()
    N = N % 26
    for i in range(len(S)):
        if ord(S[i]) + N > ord('Z'):
            print(chr(ord(S[i]) + N - 26), end='')
        else:
            print(chr(ord(S[i]) + N), end='')
