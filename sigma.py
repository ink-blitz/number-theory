

def factors(n):
    n = int(n)
    divisers = range(1, n+1)
    factors = []
    for diviser in divisers:
        if n % diviser == 0:
            factors.append(diviser)
    return factors


def sigma(n):
    sigma_of_n = 0
    for factor in factors(n):
        sigma_of_n += factor
    return sigma_of_n


def A(n):
    sigma_of_n = sigma(n)
    a_of_n = sigma_of_n / n
    return a_of_n


def sigma2(n):
    sigma2_of_n = 0
    for factor in factors(n):
        square = factor ** 2
        sigma2_of_n += square
    return sigma2_of_n


def B(n):
    sigma2_of_n = sigma2(n)
    b_of_n = sigma2_of_n / n ** 2
    return b_of_n


for x in range(1, 101):
    sigma2_of_n = sigma2(x)
    b_of_n = B(x)
    print(f"{x} - sigma2:{sigma2_of_n} B:{b_of_n}")
