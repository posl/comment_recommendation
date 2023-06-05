def is_ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True

if __name__ == '__main__':
    is_ok()