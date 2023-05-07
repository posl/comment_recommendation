def is_concatenation_of_two_copies_of_some_string(s):
    if len(s) % 2 == 0:
        if s[:len(s)//2] == s[len(s)//2:]:
            return 'Yes'
    return 'No'
