def count753(n):
    if n < 10:
        if n == 7 or n == 5 or n == 3:
            return 1
        else:
            return 0
    else:
        a = n % 10
        b = n // 10
        return count753(a) + count753(b)
N = int(input())
print(count753(N))

if __name__ == '__main__':
    count753()