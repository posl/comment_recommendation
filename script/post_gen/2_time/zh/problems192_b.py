Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 2

def main():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 3

def main():
    x = int(input())
    print(100 - x%100)
    return

=======
Suggestion 4

def get_next_prize_coin_num(coin_num):
    if coin_num % 100 == 0:
        return 100
    else:
        return 100 - (coin_num % 100)

=======
Suggestion 5

def get_next_reward_coin_num(current_coin_num):
    return (100 - current_coin_num % 100) % 100

=======
Suggestion 6

def main():
    x = int(input())
    if x % 100 == 0:
        print(100)
    else:
        print(100 - x % 100)

=======
Suggestion 7

def problem192_a():
    x = int(input())
    print(100 - x % 100)

problem192_a()
