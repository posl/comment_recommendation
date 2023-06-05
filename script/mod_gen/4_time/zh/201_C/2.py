def is_valid_pin(pin, s):
    for i in range(10):
        if s[i] == 'o' and str(i) not in pin:
            return False
        if s[i] == 'x' and str(i) in pin:
            return False
    return True
s = input()
ans = 0
for i in range(10000):
    pin = '{:04d}'.format(i)
    if is_valid_pin(pin, s):
        ans += 1
print(ans)

if __name__ == '__main__':
    is_valid_pin()