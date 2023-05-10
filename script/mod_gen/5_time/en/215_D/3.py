def gcd(a, b):
    if a % b == 0:
        return(b)
    else:
        return(gcd(b, a % b))
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A_max = A[-1]
A_min = A[0]
gcd_list = []
for i in range(1, M+1):
    if i % A_min == 0:
        gcd_list.append(i)
    else:
        for j in range(i, A_max+1, i):
            if j in A:
                break
        else:
            gcd_list.append(i)
print(len(gcd_list))
for i in gcd_list:
    print(i)

if __name__ == '__main__':
    gcd()