def solve(n, k, a):
    #print("n: {0}, k: {1}, a: {2}".format(n, k, a))
    if n == 2:
        if a[0] > a[1]:
            return False
        else:
            return True
    else:
        if k == 1:
            if a[0] > a[1]:
                return False
            else:
                return True
        else:
            for i in range(n-k):
                if a[i] > a[i+k]:
                    return False
            return True

if __name__ == '__main__':
    solve()