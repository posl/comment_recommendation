def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print('Yes' if S.count('For') > S.count('Against') else 'No')
