def solve():
    A, B = map(int, input().split())
    #print(A, B)
    #print(A/B)
    #print(A**0.5)
    #print(A**0.5/B)
    if A**0.5/B < 1:
        print(A**0.5)
    else:
        print(A**0.5/B)
