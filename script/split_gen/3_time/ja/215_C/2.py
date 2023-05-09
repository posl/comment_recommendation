def main():
    S,K = input().split()
    K = int(K)
    #print(S,K)
    S = list(S)
    S.sort()
    #print(S)
    for i in range(K-1):
        S = next_permutation(S)
    print("".join(S))
