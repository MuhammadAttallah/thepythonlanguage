def is_palindrome(s):

    original_string = s
    reversed_string = reverse(s)

    if original_string == reversed_string:
        # is palindrome
        return True

    # not a palindrome
    return False


# reverse a string
# O(N) linear running time , where N is the number of characters in the given string

def reverse(given_string):
    # convert give string into a list of characters
    nums = list(given_string)

    # pointing to the first and last indicies
    start_index = 0
    end_index = len(nums) - 1

    # swapping elements as end_index > start_index
    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1

    # converted it back to string
    return ''.join(nums)

if __name__ == "__main__":
    print(is_palindrome("radar"))