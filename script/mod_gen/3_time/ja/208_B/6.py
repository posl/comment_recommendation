def main():
    P = int(input())
    A = [1]
    for i in range(1, 11):
        A.append(A[i - 1] * i)
    A.reverse()
    ans = 0
    for i in range(10):
        ans += P // A[i]
        P %= A[i]
    print(ans)
main()
