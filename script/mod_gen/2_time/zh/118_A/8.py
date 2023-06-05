def xor(a,b):
    a1 = bin(a)[2:]
    b1 = bin(b)[2:]
    if len(a1) > len(b1):
        b1 = '0'*(len(a1)-len(b1))+b1
    else:
        a1 = '0'*(len(b1)-len(a1))+a1
    result = ''
    for i in range(len(a1)):
        if a1[i] == b1[i]:
            result += '0'
        else:
            result += '1'
    return int(result,2)
N,K = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
result = 0
for i in range(K+1):
    temp = 0
    for j in range(N):
        temp += xor(i,A[j])
    if temp > result:
        result = temp
print(result)

if __name__ == '__main__':
    xor()