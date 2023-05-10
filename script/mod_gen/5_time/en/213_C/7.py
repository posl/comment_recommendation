def main():
    H,W,N = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    A = [i[0] for i in AB]
    B = [i[1] for i in AB]
    A_ = sorted(list(set(A)))
    B_ = sorted(list(set(B)))
    A_dic = {}
    B_dic = {}
    for i in range(len(A_)):
        A_dic[A_[i]] = i+1
    for i in range(len(B_)):
        B_dic[B_[i]] = i+1
    for i in range(N):
        print(A_dic[A[i]],B_dic[B[i]])

if __name__ == '__main__':
    main()