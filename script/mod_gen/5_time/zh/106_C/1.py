def func(s,k):
    #print(s,k)
    if k <= len(s):
        return s[k-1]
    else:
        return func(s,k//len(s))

if __name__ == '__main__':
    func()