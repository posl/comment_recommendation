def check():
    for i in range(1,N):
        if A[i] != A[i-1]:
            return False
    return True

if __name__ == '__main__':
    check()