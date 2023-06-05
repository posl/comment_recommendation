def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if i%2==0:
            count+=1
    print(count)
main()
