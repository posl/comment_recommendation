def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    a.sort()
    #print(a)
    max_a = a[n-1]
    #print(max_a)
    sum = 0
    for i in range(1, max_a+1):
        sum_tmp = 0
        for j in range(0, n):
            sum_tmp += i % a[j]
            #print(sum_tmp)
        if sum_tmp > sum:
            sum = sum_tmp
            #print(sum)
    print(sum)
