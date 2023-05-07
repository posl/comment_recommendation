def path(N, A, B):
    minTime = 10**9
    for i in range(N):
        for j in range(N):
            if i == j:
                minTime = min(minTime, A[i] + B[j])
            else:
                minTime = min(minTime, max(A[i], B[j]))
    return minTime
N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
print(path(N, A, B))
I have a question regarding the time complexity of this solution. I believe that the time complexity should be O(N^2) because there are two nested for loops. Is this correct?
Yes, I think so. You can check the complexity of the min() and max() functions in Python to make sure, though.
The max() and min() functions are O(N) in Python.
Thanks for contributing an answer to Code Golf Stack Exchange!
Sign up using Email and Password

if __name__ == '__main__':
    path()