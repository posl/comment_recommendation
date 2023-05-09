def main():
    N = int(input())
    A = list(map(int, input().split()))
    dic = {}
    for a in A:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    sum = 0
    for k, v in dic.items():
        sum += v * (v-1) // 2
    for a in A:
        print(sum - (dic[a] - 1))
