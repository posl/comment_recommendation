def find_nearest_number(x, p_list):
    if x not in p_list:
        return x
    else:
        return find_nearest_number(x+1, p_list)
x, n = map(int, input().split())
p_list = list(map(int, input().split()))
print(find_nearest_number(x, p_list))

if __name__ == '__main__':
    find_nearest_number()