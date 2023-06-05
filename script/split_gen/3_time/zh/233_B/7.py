def reverse_string(string, l, r):
    return string[:l-1] + string[l-1:r][::-1] + string[r:]
