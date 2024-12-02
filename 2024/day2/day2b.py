#init ans
ans = 0

#first condition, must be increasing or decreasing.
#second condition, difference must be 1, 2 or 3.
#third condition, one instance of failed condition 1 or 2 is acceptable.
def is_safe(nums):
    
    inc = nums[0] < nums[1]
    dec = nums[0] > nums[1]
    equal = nums[0] == nums[1]

    if inc:
        for i in range(0, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
            elif (nums[i + 1] - nums[i]) not in [1, 2, 3]:
                return False
    elif dec:
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                return False
            elif (nums[i] - nums[i + 1]) not in [1, 2, 3]:
                return False
    elif equal:
        return False
    
    return True
    
def is_safe_with_removal(nums):
    #remove 1 number and check if safe
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        if is_safe(new_nums):
            return True
    return False
            
#input into list
with open("input.txt", "r") as f:
    for line in f.readlines():
        #list of nums for each line
        nums = [int(i) for i in line.split()]
        if is_safe(nums):
            ans += 1
        elif is_safe_with_removal(nums):
            ans += 1

print(ans)