def read_ints():
    return list(map(int, input().split()))
N,M,T = read_ints()
A = read_ints()
XY = [read_ints() for _ in range(M)]
time = T
prev = 0
for i in range(N-1):
    time = time - (A[i] - prev)
    prev = A[i]
    if time <= 0:
        print("No")
        exit()
    for j in range(M):
        if i+1 == XY[j][0]:
            time = time + XY[j][1]
            break
print("Yes")
