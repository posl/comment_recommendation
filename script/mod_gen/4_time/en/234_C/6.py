def findKthInteger(k):
    k -= 1
    ans = ""
    while k:
        ans += str(k % 2 * 2)
        k //= 2
    return ans[::-1].replace("0", "2")
k = int(input())
print(findKthInteger(k))

if __name__ == '__main__':
    findKthInteger()