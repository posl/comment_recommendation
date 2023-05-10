def get_permutation(string, k):
    if len(string) == 1:
        return string
    num = 1
    for i in range(1, len(string)):
        num *= i
    idx = k // num
    return string[idx] + get_permutation(string[:idx] + string[idx + 1:], k % num)
s, k = input().split()
k = int(k)
print(get_permutation(sorted(s), k - 1))

if __name__ == '__main__':
    get_permutation()