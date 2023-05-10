def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            #print("i, j", i, j)
            for k in range(j+1, n):
                #print("i, j, k", i, j, k)
                if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                    #print("l[i], l[j], l[k]", l[i], l[j], l[k])
                    if l[i] + l[j] > l[k]:
                        ans += 1
    print(ans)
