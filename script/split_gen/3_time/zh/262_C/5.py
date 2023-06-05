def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a = [1,3,2,4]
    #a = [5,8,2,2,1,6,7,2,9,10]
    #n = 10
    count = 0
    for i in range(1, n):
        if a[i-1] == i:
            for j in range(i+1, n+1):
                if a[j-1] == j:
                    count += 1
    print(count)
