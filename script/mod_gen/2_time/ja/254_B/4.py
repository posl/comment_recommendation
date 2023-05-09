def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        return [1] + [pascal(n-1)[i-1] + pascal(n-1)[i] for i in range(1,n-1)] + [1]
N = int(input())
for i in range(1,N+1):
    print(*pascal(i))

if __name__ == '__main__':
    pascal()