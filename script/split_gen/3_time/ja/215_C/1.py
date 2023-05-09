def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    S = ''.join(S)
    for i in range(K-1):
        S = next_permutation(S)
    print(S)
