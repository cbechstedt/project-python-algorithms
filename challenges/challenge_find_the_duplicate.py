def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    numbers_seen = set()
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if num in numbers_seen:
            return num
        numbers_seen.add(num)

    return False
