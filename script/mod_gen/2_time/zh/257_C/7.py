def f(x):
    #print("x:",x)
    count = 0
    for i in range(n):
        if s[i] == "0":
            if x > w[i]:
                count += 1
        else:
            if x <= w[i]:
                count += 1
    return count

if __name__ == '__main__':
    f()