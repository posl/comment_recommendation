def exchange_char(str, a, b):
    str_list = list(str)
    tmp = str_list[a-1]
    str_list[a-1] = str_list[b-1]
    str_list[b-1] = tmp
    return ''.join(str_list)
str = input()
a, b = map(int, input().split())
print(exchange_char(str, a, b))

if __name__ == '__main__':
    exchange_char()