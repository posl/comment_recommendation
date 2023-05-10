def find_friends_with_secret(N, X, A):
    friends_with_secret = 1
    friend = X
    while True:
        friend = A[friend - 1]
        if friend == X:
            break
        friends_with_secret += 1
    return friends_with_secret
