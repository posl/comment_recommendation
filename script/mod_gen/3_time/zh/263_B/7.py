def get_generation(p, generation):
    if p == 1:
        return generation
    else:
        return get_generation(p_list[p-2], generation+1)
N = int(input())
p_list = list(map(int, input().split()))
print(get_generation(p_list[-1], 1))
