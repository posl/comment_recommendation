def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    A.sort()
    #print(A)
    #print(len(A))
    sum = 0
    for i in range(len(A)-1):
        sum += i+1
    print(sum)
