def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)
N = int(input())
print(' '.join(map(str, seq(N))))

if __name__ == '__main__':
    seq()