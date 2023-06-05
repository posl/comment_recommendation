def test_219_a():
    input = 56
    output = 14
    assert output == solve(input)
    input = 32
    output = 8
    assert output == solve(input)
    input = 0
    output = 40
    assert output == solve(input)
    input = 100
    output = '专家'
    assert output == solve(input)

if __name__ == '__main__':
    test_219_a()