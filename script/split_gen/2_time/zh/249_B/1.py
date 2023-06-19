def is_wonderful_str(str):
    len_str = len(str)
    if len_str < 2 or len_str > 100:
        return False
    if str.islower() or str.isupper():
        return False
    if str.isalnum():
        return False
    if str.isalpha():
        return True
