def run():
    N = int(input())
    A = [int(x) for x in input().split()]
    #print(N, A)
    S = sum(A)
    #print(S)
    #print(A)
    #print(A[:2])
    #print(A[2:])
    #print(A[:-2])
    #print(A[-2:])
    cut1 = [A[0:1], A[1:]]
    cut2 = [A[:-1], A[-1:]]
    #print(cut1)
    #print(cut2)
    #print(cut1[0], cut1[1], cut2[0], cut2[1])
    sum1 = sum(cut1[0]) + sum(cut1[1])
    sum2 = sum(cut2[0]) + sum(cut2[1])
    #print(sum1, sum2)
    print(max(sum1, sum2) - min(sum1, sum2))

if __name__ == '__main__':
    run()