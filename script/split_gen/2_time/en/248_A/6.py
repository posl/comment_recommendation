def main():
    num_str = input()
    num_list = [int(n) for n in num_str]
    result = 45 - sum(num_list)
    print(result)
