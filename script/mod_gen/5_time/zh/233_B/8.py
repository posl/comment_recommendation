def reverse_string(l,r,s):
    s1 = s[:l-1]
    s2 = s[l-1:r]
    s3 = s[r:]
    s2 = s2[::-1]
    return s1+s2+s3

if __name__ == '__main__':
    reverse_string()