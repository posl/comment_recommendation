def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print("N",N)
    #print("A",A)
    #print("len(A)",len(A))
    #print("len(A)//2",len(A)//2)
    min_count = 0
    for i in range(len(A)//2):
        #print("i",i)
        #print("A[i]",A[i])
        #print("A[-i-1]",A[-i-1])
        if A[i] == A[-i-1]:
            continue
        elif A[i] != A[-i-1]:
            #print("min_count",min_count)
            min_count += 1
    print(min_count)
