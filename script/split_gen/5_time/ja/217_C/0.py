def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 5
    a = [5,3,2,4,1]
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    print(b)
