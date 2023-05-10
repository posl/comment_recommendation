def is_palindrome(N):
    N = str(N)
    if N == N[::-1]:
        return True
    else:
        return False
N = int(input())

if __name__ == '__main__':
    is_palindrome()