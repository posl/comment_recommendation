def baseK_to_base10(s,k):
    s = s[::-1]
    result = 0
    for i in range(len(s)):
        result += int(s[i])*(k**i)
    return result
k = int(input())
a,b = map(str,input().split())
a = baseK_to_base10(a,k)
b = baseK_to_base10(b,k)
print(a*b)

if __name__ == '__main__':
    baseK_to_base10()