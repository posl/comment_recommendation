def main():
    N,A,B = map(int, input().split())
    S = input()
    #print(S)
    #print(N,A,B)
    #判断是否是回文
    def is_huiwen(S):
        if S == S[::-1]:
            return True
        else:
            return False
    #print(is_huiwen(S))
    #判断回文的个数
    def huiwen_count(S):
        count = 0
        for i in range(N//2):
            if S[i] != S[N-i-1]:
                count += 1
        return count
    #print(huiwen_count(S))
    if is_huiwen(S):
        print(A*N+B*(huiwen_count(S)//2))
    else:
        print(A*N+B*huiwen_count(S))

if __name__ == '__main__':
    main()