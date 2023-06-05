def get_min_spell_number(n, x, y):
    min_spell_number = n
    for i in range(n):
        for j in range(i+1, n):
            spell_number = 0
            for k in range(n):
                if k != i and k != j:
                    if (x[k]-x[i])*(y[j]-y[i]) == (x[j]-x[i])*(y[k]-y[i]):
                        spell_number += 1
            if spell_number < min_spell_number:
                min_spell_number = spell_number
    return min_spell_number

if __name__ == '__main__':
    get_min_spell_number()