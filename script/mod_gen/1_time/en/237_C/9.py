def is_palindrome(s):
    return s == s[::-1]
S = input()
N = len(S)
S_rev = S[::-1]
S_rev_a = S_rev[:N//2]
S_a = S[:N//2]

if __name__ == '__main__':
    is_palindrome()