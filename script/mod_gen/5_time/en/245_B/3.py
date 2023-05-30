def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1)  
                               if x not in lst] 
N = int(input())
A = list(map(int, input().split()))
A.sort()
B = find_missing(A)
