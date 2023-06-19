def getNthSmallestNumber(k):
    if k == 1:
        return "2"
    if k == 2:
        return "20"
    if k == 3:
        return "22"
    k -= 3
    digits = 1
    while k > 2 * (2 ** digits):
        k -= 2 * (2 ** digits)
        digits += 1
    if k % 2 == 0:
        return getNthSmallestNumber(k // 2) + "0" * digits
    else:
        return getNthSmallestNumber(k // 2 + 1) + "2" + "0" * (digits - 1)
k = int(input())
print(getNthSmallestNumber(k))
