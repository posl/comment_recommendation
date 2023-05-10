def main():
    #input
    n = int(input())
    h = list(map(int, input().split()))
    #compute
    count = 1
    for i in range(1, n):
        for j in range(0, i):
            if h[j] > h[i]:
                break
        else:
            count += 1
    #output
    print(count)
