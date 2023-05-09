def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
T = int(input())
for i in range(T):
    N = int(input())
    arr = factorization(N)
    print(arr[0][0],arr[1][0])

if __name__ == '__main__':
    factorization()