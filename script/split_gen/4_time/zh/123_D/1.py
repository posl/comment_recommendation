def main():
    # 读取输入
    X, Y, Z, K = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)
    C = sorted(map(int, input().split()), reverse=True)
    # 用来记录A+B+C的和
    ABC = []
    # 用来记录A+B的和
    AB = []
    # 用来记录B+C的和
    BC = []
    # 用来记录A+C的和
    AC = []
    # 用来记录A的和
    A_ = []
    # 用来记录B的和
    B_ = []
    # 用来记录C的和
    C_ = []
    # 记录ABC的和
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ABC.append(A[i]+B[j]+C[k])
                AB.append(A[i]+B[j])
                BC.append(B[j]+C[k])
                AC.append(A[i]+C[k])
                A_.append(A[i])
                B_.append(B[j])
                C_.append(C[k])
    # 排序
    ABC.sort(reverse=True)
    AB.sort(reverse=True)
    BC.sort(reverse=True)
    AC.sort(reverse=True)
    A_.sort(reverse=True)
    B_.sort(reverse=True)
    C_.sort(reverse=True)
    # 用来记录已经输出的ABC的和的个数
    count = 0
    # 用来记录已经输出的AB的和的个数
    count_AB = 0
    # 用来记录已经输出的BC的和的个数
    count_BC = 0
    # 用来记录已经输出的AC的和的个数
    count_AC = 0
    # 用来记录已经输出的A的和的个数
    count_A = 0
    # 用来记录已经输出的B的和的个数
    count_B = 0
    # 用来记录已经输出的C的和的个数
    count_C = 0
    # 输出
    for i in range(K):
        # 记录ABC的和
