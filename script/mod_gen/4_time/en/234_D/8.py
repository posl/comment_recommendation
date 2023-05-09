def get_kth_greatest_value_of_first_i_terms_of_p(p, k, i):
    return sorted(p[:i], reverse=True)[k-1]

if __name__ == '__main__':
    get_kth_greatest_value_of_first_i_terms_of_p()