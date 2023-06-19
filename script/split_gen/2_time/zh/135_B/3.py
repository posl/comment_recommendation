def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N, p)
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")
