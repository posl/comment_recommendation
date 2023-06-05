def main():
    n = int(input())
    S = input()
    S = S.upper()
    s_list = list(S)
    for i in range(len(s_list)):
        s_list[i] = chr(ord(s_list[i]) + n)
        if ord(s_list[i]) > ord('Z'):
            s_list[i] = chr(ord(s_list[i]) - ord('Z') + ord('A') - 1)
    print(''.join(s_list))
