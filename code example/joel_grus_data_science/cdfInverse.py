#### cdf inverse implementation ####
from normalcdf  import normal_cdf
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu!= 0 or sigma!=1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z, low_p = -10.0, 0
    hi_z, hi_p   =  10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

print(inverse_normal_cdf(2))