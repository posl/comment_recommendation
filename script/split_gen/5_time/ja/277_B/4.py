def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    if len(set(S)) == len(S):
        print('Yes')
    else:
        print('No')
