def roundoff(x, k):
    for i in range(1, k+1):
        x = int(x / (10**i)) * (10**i)
    return x
x, k = map(int, input().split())
print(roundoff(x, k))

if __name__ == '__main__':
    roundoff()