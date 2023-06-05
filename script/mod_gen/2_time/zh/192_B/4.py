def get_next_reward_coin_num(current_coin_num):
    return (100 - current_coin_num % 100) % 100

if __name__ == '__main__':
    get_next_reward_coin_num()