def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [17, 51, 52, 31, 28, 47, 50, 61, 43, 65]
sort(nums)

print(nums)