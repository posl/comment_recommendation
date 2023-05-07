def replace_all(S, a, b):
    return b.join(S.split(a))
N = int(input())
S = input()
print(replace_all(S, 'na', 'nya'))
