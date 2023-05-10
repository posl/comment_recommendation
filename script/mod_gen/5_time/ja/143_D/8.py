def check(a,b,c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False
N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
#print(L)
count = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(L[i],L[j],L[k]):
                count += 1
print(count)

if __name__ == '__main__':
    check()