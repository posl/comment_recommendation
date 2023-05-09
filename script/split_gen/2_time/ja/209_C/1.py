def main():
    N = int(input())
    C = list(map(int, input().split()))
    if N == 2:
        if C[0] == C[1]:
            print(2)
        else:
            print(1)
        return
    # 1番目の要素は必ず1
    A = [1]
    # 1番目の要素を決めたので、2番目以降の要素を決める
    for i in range(1, N):
        # 1番目の要素が決まっているので、2番目以降の要素は1番目の要素より小さくならない
        if A[i-1] > C[i]:
            print(0)
            return
        # 1番目の要素が決まっているので、2番目以降の要素は1番目の要素と同じにならない
        if A[i-1] == C[i]:
            A.append(A[i-1])
        else:
            A.append(A[i-1]+1)
    print(A[-1])
