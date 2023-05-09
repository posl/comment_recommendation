def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        print(B[N//2] - A[N//2] + 1)
    else:
        print(min(B[N//2-1] + B[N//2], B[N//2] + B[N//2+1]) - max(A[N//2-1] + A[N//2], A[N//2] + A[N//2+1]) + 1)
main()
I am new to programming and I am having a hard time understanding why the second sample input has the answer 5. I thought that the optimal solution was to assign both works to Employee 2, which would take 9 minutes.
Hi @richardhuang,
The question is asking for the shortest possible time needed to complete the works. The optimal solution is to assign both works to Employee 2. However, the time it takes for Employee 2 to complete the works is 9 minutes, which is not the shortest possible time needed to complete the works. The shortest possible time needed to complete the works is 5 minutes, which is the longer of the times it takes for Employee 1 to do Work A and for Employee 2 to do Work B.
Hope this helps!
Hi @richardhuang,
The question is asking for the shortest possible time needed to complete the works. The optimal solution is to assign both works to Employee 2. However, the time it takes for Employee 2 to complete the works is 9 minutes, which is not the shortest possible time needed to complete the works. The shortest possible time needed to complete the works is 5 minutes, which is the longer of the times it takes for Employee 1 to do Work A and for Employee 2 to do Work B.
Hope this helps!
Thank you so much for the explanation! I understand now.
I am new to programming and I am having a hard time understanding why the second sample input has the answer 5. I thought that the optimal solution was to assign both works to Employee 2, which would take 9 minutes.
Hi @richardhuang,
The question is asking for the shortest possible time needed to complete the works. The optimal
