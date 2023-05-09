def is_ok(K,A,B):
    for i in range(A,B+1):
        if i%K==0:
            return True
    return False

if __name__ == '__main__':
    is_ok()