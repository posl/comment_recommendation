def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)
n = int(input())
print(' '.join(map(str,seq(n))))

if __name__ == '__main__':
    seq()