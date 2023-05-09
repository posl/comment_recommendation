def nine_multiple(n):
    n_list = list(map(int, str(n)))
    if sum(n_list) % 9 == 0:
        return 'Yes'
    else:
        return 'No'
n = int(input())
print(nine_multiple(n))
