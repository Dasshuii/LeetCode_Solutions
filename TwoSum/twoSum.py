

def twoSum(nums, target):
    values = {}
    for index, value in enumerate(nums):
        if target - value in values:
            return [index, values[target - value]]
        values[value] = index

def main():
    nums = [3, 2, 4]
    target = 6

    print(twoSum(nums, target))

if __name__ == '__main__':
    main()