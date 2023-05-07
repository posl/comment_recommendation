def main():
    K = int(input())
    keta = 1
    ans = []
    while len(ans) < K:
        for i in range(1, 10):
            if i * keta > 10 ** 15:
                break
            ans.append(i * keta)
        keta *= 10
    ans.sort()
    for i in range(K):
        print(ans[i])
