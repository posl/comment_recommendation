def get_permutation(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            result.extend([s[i] + p for p in get_permutation(s[:i] + s[i+1:])])
        return result
s = input()
permutation_list = get_permutation(s)
print(min(permutation_list))

if __name__ == '__main__':
    get_permutation()