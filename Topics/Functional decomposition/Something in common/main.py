def calculate_linear(k, b, x):
    common_part(k * x + b)


def calculate_quadratic(a, b, c, x):
    common_part((a * x * x) + (b * x) + c)


def common_part(y):
    print("Value of the function equals", y)
