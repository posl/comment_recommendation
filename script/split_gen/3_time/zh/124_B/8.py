def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(1,n+1):
        if i == 1:
            count += 1
        else:
            for j in range(1,i):
                if h[j-1] > h[i-1]:
                    break
                if j == i-1:
                    count += 1
    print(count)
