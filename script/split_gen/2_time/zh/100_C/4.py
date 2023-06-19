def main():
    #print("start")
    N = int(input())
    a = list(map(int,input().split()))
    #print(N)
    #print(a)
    #print("end")
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)
    return 0
