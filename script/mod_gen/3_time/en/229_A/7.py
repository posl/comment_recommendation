def is_connected(S1, S2):
    if S1[0] == S1[1] == S2[0] == S2[1] == '.':
        return False
    if S1[0] == S1[1] == S2[0] == S2[1] == '#':
        return True
    if S1[0] == S1[1] == '.':
        return False
    if S2[0] == S2[1] == '.':
        return False
    if S1[0] == S2[0] == '.':
        return False
    if S1[1] == S2[1] == '.':
        return False
    if S1[0] == S2[0] == '#':
        return True
    if S1[1] == S2[1] == '#':
        return True
    return True
S1 = input()
S2 = input()

if __name__ == '__main__':
    is_connected()