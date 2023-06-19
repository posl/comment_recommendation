def pascal(n):
    if n == 0:
        return [1]
    else:
        return [1] + [pascal(n-1)[i] + pascal(n-1)[i+1] for i in range(len(pascal(n-1))-1)] + [1]
n = int(input())
for i in range(n):
    print(*pascal(i))
