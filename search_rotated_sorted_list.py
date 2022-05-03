#for performing tests
test_cases = [
    {'input': {'list': [5, 6, 9, 0, 2, 3, 4], 'target': 0}, 'output': 3},
    {'input': {'list': [3, 1], 'target': 1}, 'output': 1},
    {'input': {'list': [4,5,6,7,0,1,2], 'target': 0}, 'output': 4}
]


def search_rotated_sorted_list(list, target):

        lo_index = 0
        hi_index = len(list)-1

        while lo_index<=hi_index:
            mid_index = (lo_index + hi_index) // 2
            print(list, target, mid_index)

            if list[mid_index] == target:
                return mid_index

            #Left sorted portion
            elif list[lo_index] <= list[mid_index]:
                if target > list[mid_index] or target < list[lo_index]:
                    lo_index = mid_index + 1
                else:
                    hi_index = mid_index - 1

            # Right sorted portion
            else:
                if target > list[hi_index] or target < list[mid_index]:
                    hi_index = mid_index -1
                else:
                    lo_index = mid_index + 1
        return -1


def evaluate_test_cases():
    for test_case in test_cases:
        pass_status = ''
        results = search_rotated_sorted_list(**test_case["input"])
        if results == test_case["output"]:
            pass_status = "PASSED"
        else:
            pass_status = "FAILED"
        print(f"input: {test_case['input']}, expected output,: {test_case['output']}, actual output: {results}, {pass_status}")



evaluate_test_cases()