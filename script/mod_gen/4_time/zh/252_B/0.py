def solution(N, K, A, B):
    # 1. 首先找出最大的那个食物
    maxA = max(A)
    # 2. 找出最大的那个食物的索引
    maxAIndex = A.index(maxA)
    # 3. 判断这个索引是否在B中
    if maxAIndex+1 in B:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    solution()