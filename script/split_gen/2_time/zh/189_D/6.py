def main():
    n = int(input())
    arr = list(map(int,input().split()))
    max = 0
    for i in range(n):
        for j in range(i,n):
            min = 100000
            for k in range(i,j+1):
                if arr[k] < min:
                    min = arr[k]
            if max < min*(j-i+1):
                max = min*(j-i+1)
    print(max)
