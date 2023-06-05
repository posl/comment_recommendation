def main():
    S = input()
    #print(S)
    Q = S.count('?')
    #print(Q)
    len_S = len(S)
    #print(len_S)
    cnt = 0
    for i in range(len_S):
        if S[i] == 'A':
            cnt += (pow(3,Q) * pow(3,i)) % 1000000007
        elif S[i] == 'B':
            cnt += (pow(3,Q) * pow(3,i) * 2) % 1000000007
        elif S[i] == 'C':
            cnt += (pow(3,Q) * pow(3,i) * 4) % 1000000007
        else:
            cnt += (pow(3,Q) * pow(3,i) * 3) % 1000000007
    print(cnt % 1000000007)
main()
