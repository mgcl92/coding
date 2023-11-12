from itertools import combinations


def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Given a list of integers, returns a list of elements a, b, c such that a + b + c = 0
    :param nums: list of integers
    :return: 任意连续的三个加和为 0 的元素
    """
    rst = []
    temp_list = nums[:]
    win = []

    if len(temp_list) > 2:
        win.append(temp_list.pop(0))

    while temp_list != 0:
        # 将列表首元素弹出，并压入窗口 win 末尾
        win.append(temp_list.pop(0))
        if sum(win) == 0:
            rst.append(win)
        # 弹出窗口 win 中首元素
        win.pop(0)

    return rst


def any_triplets_with_0_sum(nums: list) -> list[list[int]]:
    return [
        list(x) for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})
    ]
