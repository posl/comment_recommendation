def main():
    S = input()
    K = int(input())
    for i in range(K):
        S = S.replace('1', '11')
        S = S.replace('2', '22')
        S = S.replace('3', '33')
        S = S.replace('4', '44')
        S = S.replace('5', '55')
        S = S.replace('6', '66')
        S = S.replace('7', '77')
        S = S.replace('8', '88')
        S = S.replace('9', '99')
        if len(S) >= K:
            break
    print(S[K-1])
