import os
from time import sleep
def nextPermutation(nums) :
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    res = []
    for num in nums:
        res.append(num)
    return res

def try_answer(nums):
    with open('try.txt','w') as fp:
        fp.write('I turned the moon into something I call a Death Star.\n1 2 4 8 16 32\n1 718\n108 2\n*$/%&\'\n')
        fp.write(" ".join(nums)+"\n")
        fp.close()
    output = os.popen("./bomb try.txt")
    string = output.read()
    # print(string)
    if "BOOM!!!" in string:
        return False
    return True

def getAllAnswer():
    cur_permutation = ['1','2','3','4','5','6']
    while not try_answer(cur_permutation):
        sleep(1)
        cur_permutation = nextPermutation(cur_permutation)
    print("right answer : ")
    print(cur_permutation)


# print("test")
getAllAnswer()
# print("test")