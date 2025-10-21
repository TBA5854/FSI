"""
Octagonal membership function validator and output function.
"""


def validate_octagonal_params(h: tuple[float, float, float, float, float, float, float, float],
                              k1: float, k2: float,
                              omega1: float, omega2: float) -> bool:
    """
    Validate parameters for octagonal membership function.
    
    Parameters must satisfy: h[0] ≤ h[1] ≤ h[2] ≤ h[3] ≤ h[4] ≤ h[5] ≤ h[6] ≤ h[7]
    and 0 ≤ k1, k2 ≤ 1, 0 ≤ omega1, omega2 ≤ 1
    """
    # Check ordering of h parameters
    if not (h[0] <= h[1] <= h[2] <= h[3] <= h[4] <= h[5] <= h[6] <= h[7]):
        return False
    
    # Check k parameters are in [0, 1]
    if not (0 <= k1 <= 1 and 0 <= k2 <= 1):
        return False
    
    # Check omega parameters are in [0, 1]
    if not (0 <= omega1 <= 1 and 0 <= omega2 <= 1):
        return False
    
    return True


def octagonal_membership(x: float,
                         h: tuple[float, float, float, float, float, float, float, float],
                         k1: float, k2: float,
                         omega1: float, omega2: float) -> float:
    """
    Compute octagonal membership function value.
    
    Args:
        x: Input value
        h: Tuple of 8 boundary parameters (h[0] through h[7])
        k1, k2: Height parameters
        omega1, omega2: Weight parameters
    
    Returns:
        Membership value in [0, 1]
    """
    if not validate_octagonal_params(h, k1, k2, omega1, omega2):
        raise ValueError("Invalid octagonal parameters")
    
    # Region 1: x ≤ h[0] → 0
    if x <= h[0]:
        return 0.0
    
    # Region 2: h[0] < x ≤ h[1]
    if x <= h[1]:
        if h[1] > h[0]:
            return ((x - h[0]) / (h[1] - h[0])) * (k1 - omega1)
        return 0.0
    
    # Region 3: h[1] < x ≤ h[2]
    if x <= h[2]:
        return k1 - omega1
    
    # Region 4: h[2] < x ≤ h[3]
    if x <= h[3]:
        if h[3] > h[2]:
            return (k1 - omega1) + ((x - h[2]) / (h[3] - h[2])) * omega1
        return k1 - omega1
    
    # Region 5: h[3] < x ≤ h[4]
    if x <= h[4]:
        return k1
    
    # Region 6: h[4] < x ≤ h[5]
    if x <= h[5]:
        if h[5] > h[4]:
            return k1 - ((x - h[4]) / (h[5] - h[4])) * (k1 - k2 + omega2)
        return k1
    
    # Region 7: h[5] < x ≤ h[6]
    if x <= h[6]:
        return k2 - omega2
    
    # Region 8: h[6] < x ≤ h[7]
    if x <= h[7]:
        if h[7] > h[6]:
            return ((h[7] - x) / (h[7] - h[6])) * (k2 - omega2)
        return k2 - omega2
    
    # Region 9: x > h[7] → 0
    return 0.0
