def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #print(a)
    #print(b)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    #print(sum)
    if sum == 0:
        print("Yes")
    else:
        print("No")
