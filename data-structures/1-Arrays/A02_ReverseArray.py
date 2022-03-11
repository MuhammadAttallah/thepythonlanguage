# reverse an array
def reverse(nums):
    # pointing to the first and last indicies
    start_index = 0
    end_index = len(nums) - 1

    # swapping elements as end_index > start_index
    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1

if __name__ == "__main__":
    n1 = [5, 4, 3, 2, 1]
    reverse(n1)
    print(n1)