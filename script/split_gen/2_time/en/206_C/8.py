def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(1)
        return
    A.sort()
    #print(A)
    ans = 0
    for i in range(1, N):
        if A[i] == A[i-1]:
            ans += N - i
    print(ans)
main()
This is a problem that I couldn't solve by myself. I couldn't figure out the logic.
I tried to solve this problem by using a dictionary. However, I couldn't solve it.
I tried to solve this problem by using a set. However, I couldn't solve it.
I tried to solve this problem by using a list. However, I couldn't solve it.
I tried to solve this problem by using a list and a dictionary. However, I couldn't solve it.
I tried to solve this problem by using a list and a set. However, I couldn't solve it.
I tried to solve this problem by using a list and a list. However, I couldn't solve it.
I tried to solve this problem by using a dictionary and a dictionary. However, I couldn't solve it.
I tried to solve this problem by using a dictionary and a set. However, I couldn't solve it.
I tried to solve this problem by using a dictionary and a list. However, I couldn't solve it.
I tried to solve this problem by using a set and a set. However, I couldn't solve it.
I tried to solve this problem by using a set and a list. However, I couldn't solve it.
I tried to solve this problem by using a set and a dictionary. However, I couldn't solve it.
I tried to solve this problem by using a list and a list. However, I couldn't solve it.
I tried to solve this problem by using a list and a dictionary. However, I couldn't solve it.
I tried to solve this problem by using a list and a set. However, I couldn't solve it.
I tried to solve this problem by using a list and a list. However, I couldn't solve it.
I tried to solve this problem by using a dictionary and a dictionary. However, I couldn't solve it.
I tried to solve this problem by using a dictionary and a set. However, I couldn't solve it.
I tried to solve this problem by using a dictionary
