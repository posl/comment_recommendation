def findKthChar(s, k):
    l = len(s)
    if l >= k:
        return s[k - 1]
    else:
        return '1' if s[-1] == '1' else '9'
s = input()
k = int(input())
print(findKthChar(s, k))

if __name__ == '__main__':
    findKthChar()