def get_good_number(N,W,A):
    # N = int(input("请输入砝码的个数："))
    # W = int(input("请输入砝码的总重量："))
    # A = list(map(int,input("请输入砝码的重量：").split()))
    A.sort()
    # print(A)
    # print(N,W,A)
    good_number = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if A[i]+A[j]+A[k] <= W:
                    good_number += 1
                else:
                    break
    return good_number

if __name__ == '__main__':
    get_good_number()