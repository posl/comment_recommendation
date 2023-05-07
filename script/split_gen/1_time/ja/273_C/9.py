def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)
    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)
    #countを累積和の形にする
    count_sum = [0]
    for i in range(len(count)):
        count_sum.append(count_sum[i]+count[i])
    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)
    #countを累積和の形にする
    count_sum = [0]
    for i in range(len(count)):
        count_sum.append(count_sum[i]+count[i])
    #count_sumを累積和の形にする
    count_sum_sum = [0]
    for i in range(len(count_sum)):
        count_sum_sum.append(count_sum_sum[i]+count_sum[i])
    #Aの値ごとに個数を数える
    count = []
    for i in range(N):
        if i == 0:
            count.append(1)
        elif A[i] == A[i-1]:
            count[-1] += 1
        else:
            count.append(1)
    #countを累積和の形にする
    count_sum = [0]
    for i in range(len(count)):
        count_sum.append(count_sum[i]+count[i])
    #count_sumを累積和の形にする
    count_sum_sum = [0]
    for i in range(len(count_sum)):
