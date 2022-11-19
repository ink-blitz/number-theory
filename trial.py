

def factors(n):
    n = int(n)
    divisers = range(1, n+1)
    factors = []
    for diviser in divisers:
        if n % diviser == 0:
            factors.append(diviser)
    return factors


def sigma2(n):
    sigma2_of_n = 0
    for factor in factors(n):
        square = factor ** 2
        sigma2_of_n += square
    return sigma2_of_n

print(sigma2(input(": ")))