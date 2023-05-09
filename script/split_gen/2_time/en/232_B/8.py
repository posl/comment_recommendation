def shiftByK(s, k):
    return ''.join([chr((ord(c) - ord('a') + k) % 26 + ord('a')) for c in s])
