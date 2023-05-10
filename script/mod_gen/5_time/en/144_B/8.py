def check_if_product_of_two_integers_between_1_and_9(n):
    for i in range(1, 10):
        if n % i == 0 and n / i in range(1, 10):
            return "Yes"
    return "No"

if __name__ == '__main__':
    check_if_product_of_two_integers_between_1_and_9()