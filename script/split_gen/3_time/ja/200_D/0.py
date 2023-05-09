def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = [0] * 200
    for i in range(N):
        mod[A[i] % 200] += 1
    for i in range(200):
        if mod[i] > 1:
            print("Yes")
            print(mod[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod[i] -= 1
                    if mod[i] == 0:
                        print()
                        break
            print(mod[i], end=" ")
            for j in range(N):
                if A[j] % 200 == i:
                    print(j + 1, end=" ")
                    mod[i] -= 1
                    if mod[i] == 0:
                        print()
                        break
            break
    else:
        print("No")
