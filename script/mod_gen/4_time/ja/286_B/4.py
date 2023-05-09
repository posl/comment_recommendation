def replace_na(n, s):
    if n < 2:
        return s
    else:
        return replace_na(n-1, s.replace('na'*n, 'nya'*n))
n = int(input())
s = input()
print(replace_na(n, s))

if __name__ == '__main__':
    replace_na()