def calc_xor(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] ^ calc_xor(lst[1:])
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

if __name__ == '__main__':
    calc_xor()