def get_complementary_base(base):
    if base == 'A':
        return 'T'
    if base == 'T':
        return 'A'
    if base == 'C':
        return 'G'
    if base == 'G':
        return 'C'
base = input()
print(get_complementary_base(base))
