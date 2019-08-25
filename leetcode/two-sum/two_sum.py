
from pprint import pprint

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for first_addend_index, first_addend in enumerate(nums):
        try:
            second_addend_index = nums.index(target - first_addend)
            if second_addend_index != first_addend_index:
                print([first_addend_index, second_addend_index])
        except:
            next


def two_sum_2(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                pprint(buff_dict)
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
        

two_sum([2,7,11,15], 9)

# 91% faster than all other solutions
two_sum_2([2,7,11,15], 9)
