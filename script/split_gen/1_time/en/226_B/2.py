def main():
    N = int(input())
    dic = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] in dic:
            dic[L[0]].append(L[1:])
        else:
            dic[L[0]] = [L[1:]]
    count = 0
    for i in dic:
        count += len(set(map(tuple, dic[i])))
    print(count)
