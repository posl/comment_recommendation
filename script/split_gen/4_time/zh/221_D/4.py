def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    # print(a)
    # print(b)
    i = 0
    j = 0
    k = 0
    ans = [0]*n
    while i < n:
        if a[i] <= b[j]:
            k += 1
            i += 1
        else:
            k -= 1
            j += 1
        ans[k] += 1
    print(' '.join(map(str,ans)))
