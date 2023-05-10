def check_permutation(n, a):
    if n == len(a):
        for i in range(1, n+1):
            if i not in a:
                return 'No'
        return 'Yes'
    else:
        return 'No'
n = int(input())
a = list(map(int, input().split()))
print(check_permutation(n, a))

if __name__ == '__main__':
    check_permutation()