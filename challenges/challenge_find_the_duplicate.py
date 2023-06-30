def find_duplicate(nums):
    nums.sort()
    if not nums or len(nums) < 2 or not isinstance(nums[0], int):
        return False

    checked_nums = set()
    for num in nums:
        if num < 0:
            return False
        elif num in checked_nums:
            return num
        else:
            checked_nums.add(num)
    return False

if __name__ == '__main__':
    print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))