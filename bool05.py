def main(a):
    """
    check the following statement "The variable "a" is an odd number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    var_odd = a % 2 == 1
    return var_odd
print(main(5)) 