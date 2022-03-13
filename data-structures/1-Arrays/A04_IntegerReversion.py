# reversing an integer using integer divison and modulo opertaor

def reverse_integer(n):

    reversed_int = 0
    remainder = 0

    while n > 0:

        remainder = n % 10  # get the last digit
        reversed_int = reversed_int * 10 + remainder
        n = n // 10   # integer division

    return reversed_int

if __name__ == "__main__":
    print(reverse_integer(123456789))
