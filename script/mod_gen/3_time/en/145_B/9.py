def is_concatenation_of_two_copies(s):
    n = len(s)
    if n % 2 == 1:
        return False
    else:
        t = s[:n//2]
        return s == t + t

if __name__ == '__main__':
    is_concatenation_of_two_copies()