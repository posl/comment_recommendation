def calc_temp(t, h):
    return abs(t - h * 0.006)
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
temp_list = list(map(lambda x: calc_temp(T, x), H))
print(temp_list.index(min(temp_list)) + 1)

if __name__ == '__main__':
    calc_temp()