def count_good_string(n):
    even_count = (n+1) // 2
    odd_count = n // 2

    return (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD
