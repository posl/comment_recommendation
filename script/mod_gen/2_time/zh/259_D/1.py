def diff(a,b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
s = input()
t = input()

if __name__ == '__main__':
    diff()