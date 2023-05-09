def main():
    # S = input().rstrip()
    S = input().rstrip()
    # print(S)
    # print(len(S))
    # print(S[0])
    # print(S[1])
    # print(S[2])
    # print(S[0] == S[1])
    # print(S[0] == S[2])
    # print(S[1] == S[2])
    if S[0] == S[1]:
        print(S[2])
    elif S[0] == S[2]:
        print(S[1])
    elif S[1] == S[2]:
        print(S[0])
    else:
        print('-1')
