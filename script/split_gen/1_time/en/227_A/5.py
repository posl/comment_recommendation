def get_last_person(N, K, A):
    last_person = A + K - 1
    while last_person > N:
        last_person -= N
    return last_person
N, K, A = map(int, input().split())
print(get_last_person(N, K, A))
