def main(a):
    """
    check the following statement "The variable "a" is an even number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    var_even = a % 2 == 0
    return var_even
print(main(5))