def find_even_digit_numbers(nums):
    count = 0 
    for num in nums:
        digit_count = len(str(abs(num)))
        if digit_count % 2 == 0:
            count += 1
    return count
