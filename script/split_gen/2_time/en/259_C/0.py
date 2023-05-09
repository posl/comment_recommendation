def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    if N != M:
        print("No")
        return
    for i in range(N):
        if S[i] != T[i]:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("Yes")
    return
main()
I think this is a good problem.
I solved this problem using Python3.
I got 100 points.
This is my first post.
I will continue to post my solutions.
I hope you like this article.
