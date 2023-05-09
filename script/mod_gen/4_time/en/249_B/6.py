def is_wonderful_string(S):
    if len(S) < 2:
        return False
    if S.islower() or S.isupper():
        return False
    if len(S) != len(set(S)):
        return False
    return True
S = input()

if __name__ == '__main__':
    is_wonderful_string()