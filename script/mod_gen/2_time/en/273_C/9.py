def count_greater_than_Ai(A, N):
    A.sort()
    A.append(0)
    greater_than_Ai = 1
    count_greater_than_Ai = []
    for i in range(1, N+1):
        if A[i] != A[i-1]:
            count_greater_than_Ai.append(greater_than_Ai)
            greater_than_Ai = 1
        else:
            greater_than_Ai += 1
    return count_greater_than_Ai

if __name__ == '__main__':
    count_greater_than_Ai()