def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    same = 0
    diff = 0
    for i in range(N):
        if A[i] == B[i]:
            same += 1
        else:
            for j in range(N):
                if A[i] == B[j]:
                    diff += 1
                    break
    print(same)
    print(diff)
