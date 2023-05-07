def main():
    num_of_crackers, num_of_users = map(int, input().split())
    print(num_of_crackers % num_of_users)
