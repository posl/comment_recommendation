def prefix(s, t):
    if s == t[:len(s)]:
        return 'Yes'
    else:
        return 'No'
s = input()
t = input()
print(prefix(s, t))

if __name__ == '__main__':
    prefix()