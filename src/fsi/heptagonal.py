def heptagonal_membership(
    x: float,
    h: tuple[float, float, float, float, float, float, float],
    k1: float = 1.0,
    k2: float = 1.0,
    omega1: float = 0.0,
    omega2: float = 0.0,
) -> float:
    """
    Compute heptagonal fuzzy membership function.
    
    Args:
        x: Input value
        h: Tuple of seven parameters (h1-h7) defining the heptagonal shape
        k1, k2: Height parameters (default 1.0)
        omega1, omega2: Offset parameters (default 0.0)
    
    Returns:
        Membership value in [0, max(k1, k2)]
    """
    h1, h2, h3, h4, h5, h6, h7 = h
    
    # x <= h1
    if x <= h1:
        return 0.0
    
    # h1 <= x <= h2
    if x <= h2:
        return (k1 - omega1) * (x - h1) / (h2 - h1)
    
    # h2 <= x <= h3
    if x <= h3:
        return k1 - omega1 * (x - h2) / (h3 - h2)
    
    # h3 <= x <= h4
    if x <= h4:
        return k1
    
    # h4 <= x <= h5
    if x <= h5:
        return k2 - omega2 * (h5 - x) / (h5 - h4)
    
    # h5 <= x <= h6
    if x <= h6:
        return (k2 - omega2) * (h6 - x) / (h6 - h5) + omega2
    
    # h6 <= x <= h7
    if x <= h7:
        return omega2 * (h7 - x) / (h7 - h6)
    
    # x >= h7
    return 0.0


def validate_heptagonal_params(
    h: tuple[float, float, float, float, float, float, float],
    k1: float = 1.0,
    k2: float = 1.0,
    omega1: float = 0.0,
    omega2: float = 0.0,
) -> bool:
    """
    Validate heptagonal fuzzy membership parameters.
    
    Args:
        h: Tuple of seven parameters (h1-h7) defining the heptagonal shape
        k1, k2: Height parameters
        omega1, omega2: Offset parameters
    
    Returns:
        True if parameters are valid
    
    Raises:
        ValueError: If parameters are invalid
    """
    h1, h2, h3, h4, h5, h6, h7 = h
    
    if not (h1 <= h2 <= h3 <= h4 <= h5 <= h6 <= h7):
        raise ValueError("Parameters must satisfy: h1 <= h2 <= h3 <= h4 <= h5 <= h6 <= h7")
    
    if k1 < 0 or k2 < 0:
        raise ValueError("Height parameters k1 and k2 must be non-negative")
    
    if omega1 < 0 or omega1 > k1:
        raise ValueError(f"omega1 must be in [0, k1], got omega1={omega1}, k1={k1}")
    
    if omega2 < 0 or omega2 > k2:
        raise ValueError(f"omega2 must be in [0, k2], got omega2={omega2}, k2={k2}")
    
    return True
