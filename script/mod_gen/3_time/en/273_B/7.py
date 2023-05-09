def roundoff(x):
    if x % 1000 == 0:
        return x
    else:
        return (x // 1000 + 1) * 1000

if __name__ == '__main__':
    roundoff()