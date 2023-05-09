def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    maxP = P[0]
    count = 1
    for i in range(1,N):
        if maxP > P[i]:
            count += 1
        else:
            maxP = P[i]
    print(count)
    return
