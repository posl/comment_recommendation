def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    if S.count('For') > S.count('Against'):
        print('Yes')
    else:
        print('No')
