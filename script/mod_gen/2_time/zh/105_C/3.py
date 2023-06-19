def solve(N):
    if N==0:
        return "0"
    result = ""
    while N!=0:
        if N%2==0:
            result = "0" + result
            N = N//2
        else:
            result = "1" + result
            N = (N-1)//(-2)
    return result
N = int(input())
print(solve(N))
