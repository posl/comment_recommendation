def reverse_string(str, l, r):
    return str[:l-1] + str[l-1:r][::-1] + str[r:]
