def swap_char(s, a, b):
    s_list = list(s)
    s_list[a-1], s_list[b-1] = s_list[b-1], s_list[a-1]
    return ''.join(s_list)
s = input()
a, b = map(int, input().split())
print(swap_char(s, a, b))

if __name__ == '__main__':
    swap_char()