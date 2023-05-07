def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    a[i : ] = a[len(a) - 1 : i - 1 : -1]
    return True
N = int(input())
P = list(map(int, input().split()))
for i in range(N - 1):
    if P[i] > P[i + 1]:
        break
else:
    print(" ".join(map(str, P)))
    exit()
for i in range(N - 2, -1, -1):
    if P[i] < P[i + 1]:
        break
else:
    print(" ".join(map(str, P)))
    exit()
for i in range(1, N):
    if P[i - 1] > P[i]:
        break
else:
    print(" ".join(map(str, P)))
    exit()
Q = list(range(1, N + 1))
for i in range(P[0] - 1):
    next_permutation(Q)
for i in range(N - 1):
    if P[i] > P[i + 1]:
        break
    for j in range(P[i + 1] - P[i] - 1):
        next_permutation(Q)
print(" ".join(map(str, Q)))
I have a problem with the following code. I am trying to find the next permutation of a given permutation. The code works fine for small inputs, but for large inputs it is giving me a runtime error. I am not sure what is wrong with the code. Can someone help me? Here is the code:

if __name__ == '__main__':
    next_permutation()