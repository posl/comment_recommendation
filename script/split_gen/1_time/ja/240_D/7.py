def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    cnt = 1
    for i in range(N):
        if A[i] == cnt:
            cnt += 1
        else:
            print(cnt)
    print(cnt)
    return
main()
