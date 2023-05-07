def next_permutation(s):
    """
    Find the next permutation of a string s.
    
    Args:
        s (str): a string.
    Returns:
        str: the next permutation of s, or None if s is the last permutation.
    """
    n = len(s)
    if n == 1:
        return None
    for i in range(n-2, -1, -1):
        if s[i] < s[i+1]:
            break
    else:
        return None
    for j in range(n-1, i, -1):
        if s[i] < s[j]:
            break
    s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
    s = s[:i+1] + s[i+1:][::-1]
    return s
