def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    #print(A)
    #print(X)
    #print(N)
    #print(A[X])
    #print(A)
    #print(N)
    friend = []
    friend.append(X)
    #print(friend)
    i = 0
    while True:
        if friend[i] == A[friend[i]]:
            break
        else:
            friend.append(A[friend[i]])
            #print(friend)
            i += 1
    print(len(friend))

if __name__ == '__main__':
    main()