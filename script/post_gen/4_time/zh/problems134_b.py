Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    print(N // (2 * D + 1) + (N % (2 * D + 1) > 0))

=======
Suggestion 2

def main():
    N,D = map(int,input().split())
    if N%(2*D+1)==0:
        print(N//(2*D+1))
    else:
        print(N//(2*D+1)+1)

=======
Suggestion 3

def main():
    # 读取输入
    n,d = map(int,input().split())
    # 检查员数量
    count = 0
    # 树列表
    tree = [0 for i in range(n)]
    # 读取树的信息
    for i in range(n):
        tree[i] = int(input())
    # 遍历树
    for i in range(n):
        # 检查员是否已经部署
        flag = False
        # 遍历检查员
        for j in range(count):
            # 检查员已经部署
            if tree[i] - d <= check[j] and check[j] <= tree[i] + d:
                flag = True
                break
        # 检查员未部署
        if flag == False:
            # 部署检查员
            check[count] = tree[i]
            # 检查员数量增加
            count += 1
    # 输出检查员数量
    print(count)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 6

def check_apple_tree(n, d):
    if n % (d * 2 + 1) == 0:
        return n // (d * 2 + 1)
    else:
        return n // (d * 2 + 1) + 1
