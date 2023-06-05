def reverse_string(s, l, r):
    # 1. 从s中取出l至r的子串
    substr = s[l-1:r]
    # 2. 将子串反转
    substr = substr[::-1]
    # 3. 将反转后的子串替换到原串中
    s = s[:l-1] + substr + s[r:]
    print(s)

if __name__ == '__main__':
    reverse_string()