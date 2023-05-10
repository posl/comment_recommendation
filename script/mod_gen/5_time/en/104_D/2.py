def main():
    S = input()
    A = 0
    B = 0
    C = 0
    Q = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
        else:
            Q += 1
    abc = 0
    for i in range(Q):
        abc += pow(3,i,1000000007) * (pow(3,Q-i-1,1000000007) * A * B * C % 1000000007 + pow(3,Q-i-1,1000000007) * A * B % 1000000007 + pow(3,Q-i-1,1000000007) * B * C % 1000000007 + pow(3,Q-i-1,1000000007) * C * A % 1000000007 + pow(3,Q-i-1,1000000007) * A % 1000000007 + pow(3,Q-i-1,1000000007) * B % 1000000007 + pow(3,Q-i-1,1000000007) * C % 1000000007 + pow(3,Q-i-1,1000000007) % 1000000007)
        abc %= 1000000007
    print(abc)

if __name__ == '__main__':
    main()