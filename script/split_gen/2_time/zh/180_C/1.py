def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)
    if temp!=1:
        arr.append(temp)
    if arr==[]:
        arr.append(n)
    return arr
n = int(input())
arr = factorization(n)
ans = set()
ans.add(1)
for i in range(1, len(arr)+1):
    for j in range(len(arr)):
        ans.add(arr[j]**i)
ans = sorted(list(ans))
for i in range(len(ans)):
    print(ans[i])
