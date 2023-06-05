def get_permutation(s, k):
    if len(s) == 1:
        return s
    else:
        s = sorted(s)
        # print(s)
        n = len(s)
        # print(n)
        # print(k)
        if k == 1:
            return s[0] + get_permutation(s[1:], k)
        elif k == n:
            return s[-1] + get_permutation(s[:-1], k-1)
        else:
            if k % factorial(n-1) == 0:
                return s[k//factorial(n-1)-1] + get_permutation(s[:k//factorial(n-1)-1]+s[k//factorial(n-1):], n-1)
            else:
                return s[k//factorial(n-1)] + get_permutation(s[:k//factorial(n-1)]+s[k//factorial(n-1)+1:], k%factorial(n-1))

if __name__ == '__main__':
    get_permutation()