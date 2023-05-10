def check_pasta(pasta, pasta_len):
    for i in range(len(pasta)):
        if pasta[i] == pasta_len:
            return True
    return False
