def main():
    N, Q = map(int, input().split())
    # 1-index
    follow = [[] for _ in range(N+1)]
    followed = [[] for _ in range(N+1)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A].append(B)
            followed[B].append(A)
        elif T == 2:
            if A in follow[B]:
                follow[B].remove(A)
            if B in followed[A]:
                followed[A].remove(B)
        else:
            if A in followed[B] and B in follow[A]:
                print("Yes")
            else:
                print("No")
main()
This is my solution. I created two lists, one for each direction of following. The first list is for following and the second list is for followed. Each list is indexed by the user ID. Each list contains the user ID of the users that are either following or followed by the user ID of the list.
The first two if statements are for the first two cases. The first if statement is for when the user is following another user. The second if statement is for when the user is unfollowing another user. The third if statement is for when the user is asking if two users are following each other. The third if statement checks if the user is following the other user and the other user is following the user. If both of these are true, then the user is following the other user and the other user is following the user, so the answer is Yes. Otherwise, the answer is No.

if __name__ == '__main__':
    main()