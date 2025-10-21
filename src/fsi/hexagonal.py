def validate_hexagonal_inputs(h_tuple: tuple[float], ul: float, ur: float, u: float, x: float) -> float:
    # validate inputs
    if len(h_tuple) != 6:
        raise ValueError("h_tuple must have exactly 6 elements.")

    h1, h2, h3, h4, h5, h6 = h_tuple

    if not all(h_tuple[i] <= h_tuple[i+1] for i in range(5)):
        print(h_tuple)
        raise ValueError("h_tuple values must be in strictly increasing order.")

    if not (ul < u and u > ur):
        raise ValueError("Inputs must satisfy ul < u > ur.")
    
    if not (ul < u and u > ur):
        raise ValueError("Inputs must satisfy ul < u > ur.")

    if not all(h_tuple[i] < h_tuple[i+1] for i in range(5)):
        raise ValueError("All input values must be in strictly increasing order.")

    return True

def hexagonal_fuzzer(h_tuple: tuple[float], ul: float, ur: float, u: float, x: float) -> float:
    """
    Hexagonal fuzzy set implementation.

    Parameters:
    h_tuple (tuple): A tuple of six floats (h1, h2, h3, h4, h5, h6) defining the hexagon shape.
    ul (float): The left height of the hexagon.
    ur (float): The right height of the hexagon.
    u (float): The peak height of the hexagon.
    x (float): The input value for which to compute the membership degree.

    Returns:
    float: The membership degree of x in the hexagonal fuzzy set.
    """
    # Validate inputs
    validate_hexagonal_inputs(h_tuple, ul, ur, u, x)

    h1, h2, h3, h4, h5, h6 = h_tuple

    if x < h1 or x > h6:
        return 0.0
    elif h3 <= x <= h4:
        return u
    elif h1 <= x < h2:
        return ul * (x - h1) / (h2 - h1)
    elif h5 < x <= h6:
        return ur * (h6 - x) / (h6 - h5)
    elif h2 <= x < h3:
        return ul + (u - ul) * (x - h2) / (h3 - h2)
    elif h4 < x <= h5:
        return ur + (u - ur) * (h5 - x) / (h5 - h4)