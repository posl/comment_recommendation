def main():
    S = input()
    K = int(input())
    S = S.replace('X','X.')
    S = S.split('.')
    S = [len(i) for i in S]
    S = [i for i in S if i > 0]
    if len(S) <= K:
        print(sum(S)+K-len(S))
    else:
        print(sum(S[:K])+K)
