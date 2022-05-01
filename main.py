
tests_cases = [
    {'input': {'nums': [0, 1, 3, 4, 7, 10, 11, 13], 'target': 7}, 'output': 4},
    {'input': {'nums': [0, 1, 3, 4, 7, 10, 11, 13], 'target': 1}, 'output': 1},
    {'input': {'nums': [-1, 1, 2, 4], 'target': 4}, 'output': 3},
    {'input': {'nums': [-127, -9, -1, 3], 'target': -127}, 'output': 0},
    {'input': {'nums': [6], 'target': 6}, 'output': 0},
    {'input': {'nums': [-9, 2, 5, 7, 9], 'target': 4}, 'output': -1},
    {'input': {'nums': [], 'target': 7}, 'output': -1},
    {'input': {'nums': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8], 'target': 3},
     'output': 6},
    {'input': {'nums': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8],
               'target': 6},
     'output': 7}
]


def test_occurence(nums, target, mid):
    if nums[mid] == target:
        if mid-1>0 and nums[mid-1]==target:
            return "left"
        else:
            return "found"
    elif nums[mid] < target:
        return 'right'
    elif nums[mid] > target:
        return 'left'
    else:
        return -1



def find_target(nums, target):
    lo_index = 0
    hi_index = len(nums)-1



    while lo_index<=hi_index:
        mid_index = (lo_index + hi_index) // 2
        test_occurence_output = test_occurence(nums, target, mid_index)
        if test_occurence_output == "found":
            return mid_index
        elif test_occurence_output == "right":
            lo_index = mid_index + 1
        elif test_occurence_output == "left":
            hi_index = mid_index-1
    return -1


def evaluate_test_cases():
    for test_case in tests_cases:
        pass_status = ""
        results = find_target(**test_case["input"])
        if test_case["output"] == results:
            pass_status = "PASSED"
        else:
            pass_status = "FAILED"

        print(f"input: {test_case['input']}, expected output: {test_case['output']}, actual output: {results}, {pass_status} ")



print(evaluate_test_cases())