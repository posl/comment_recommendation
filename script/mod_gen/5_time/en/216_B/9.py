def check_if_exists(s):
    if len(s) != len(set(s)):
        return True
    else:
        return False
n = int(input())
s = []
t = []
for i in range(n):
    temp_s, temp_t = input().split()
    s.append(temp_s)
    t.append(temp_t)

if __name__ == '__main__':
    check_if_exists()