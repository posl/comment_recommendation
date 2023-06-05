def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A.sort()
    A = [0] + A
    #print(N, A)
    #print(len(A))
    #print(A[1:2**N+1])
    #print(A[2**N+1:])
    def find_index(a, b):
        for i in range(1, 2**N+1):
            if A[i] == a:
                index_a = i
            if A[i] == b:
                index_b = i
        return index_a, index_b
    #print(find_index(3, 5))
    def find_second(a, b):
        if a > b:
            return A[b+1]
        else:
            return A[a+1]
    #print(find_second(3, 5))
    for i in range(N):
        a = 1
        b = 2
        for j in range(2**(N-i-1)):
            index_a, index_b = find_index(a, b)
            #print(a, b, index_a, index_b)
            if A[index_a] > A[index_b]:
                a = index_a
            else:
                a = index_b
            b += 2
        #print(a, b)
        print(find_second(a, b))
