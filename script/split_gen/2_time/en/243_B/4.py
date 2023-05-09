def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = dict()
    B_dict = dict()
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i
    same = 0
    diff = 0
    for i in range(N):
        if A[i] in B_dict:
            if i == B_dict[A[i]]:
                same += 1
            else:
                diff += 1
    print(same)
    print(diff)
