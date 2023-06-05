def move(s, k):
    return ''.join([chr((ord(x)-ord('a')+k)%26+ord('a')) for x in s])
s = input()
t = input()
for i in range(26):
    if move(s, i) == t:
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    move()