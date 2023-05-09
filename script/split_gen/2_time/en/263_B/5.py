def main():
    N = int(input())
    P = list(map(int,input().split()))
    P.insert(0,0)
    count = 0
    for i in range(N,1,-1):
        if P[i] == 1:
            count += 1
            break
        else:
            count += 1
            i = P[i]
    print(count)
