# run an A/B test to test p-hacking
import math
def estimated_parameters(N, n):

    p =n / N
    sigma  = math.sqrt(p * (1-p) / N)
    return p, sigma

def a_b_test_statistics(N_A, n_A, N_B, n_B):
    p_A,sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistics(1000, 200, 1000, 180)

print( z)