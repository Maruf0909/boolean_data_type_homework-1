def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    from math import sqrt
    perfect = sqrt(a)%2 == 1
    return perfect
print(main(15))