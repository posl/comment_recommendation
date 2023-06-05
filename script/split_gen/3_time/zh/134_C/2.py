def main():
    # 读取输入
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    # 求解并输出
    for i in range(N):
        print(max(A[0:i] + A[i+1:N]))
