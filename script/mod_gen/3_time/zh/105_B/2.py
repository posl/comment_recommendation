def func(N):
    for i in range(0, N//4+1):
        for j in range(0, N//7+1):
            if 4*i+7*j == N:
                return "Yes"
    return "No"
N = int(input())
print(func(N))
