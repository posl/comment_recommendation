def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    n_list = list(n_str)
    n_list.sort(reverse=True)
    n_str = ''.join(n_list)
    n_list = list(n_str)
    n_list.sort()
    n_str2 = ''.join(n_list)
    n_str2 = n_str2.lstrip('0')
    if n_str2 == '':
        n_str2 = '0'
    n_str = n_str.lstrip('0')
    if n_str == '':
        n_str = '0'
    print(int(n_str)*int(n_str2))
