def main():
    N = int(input())
    A = list(map(int, input().split()))
    dic = {}
    for i in range(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    total = 0
    for key in dic:
        total += dic[key] * (dic[key] - 1) // 2
    for i in range(N):
        print(total - (dic[A[i]] - 1))
