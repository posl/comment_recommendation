def main():
    # N = input()
    # S = input()
    N = 13
    S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # N = 2
    # S = "ABCXYZ"
    N = int(N)
    S = list(S)
    # print(S)
    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))
    for i in range(len(S)):
        # print(S[i])
        # print(ord(S[i]))
        # print(ord(S[i]) + N)
        # print(ord(S[i]) + N - ord('Z'))
        # print(ord(S[i]) + N - ord('Z') + ord('A'))
        if ord(S[i]) + N <= ord('Z'):
            # print(chr(ord(S[i]) + N))
            S[i] = chr(ord(S[i]) + N)
        else:
            # print(chr(ord(S[i]) + N - ord('Z') + ord('A') - 1))
            S[i] = chr(ord(S[i]) + N - ord('Z') + ord('A') - 1)
    print("".join(S))
