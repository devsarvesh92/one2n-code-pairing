def is_palindrome(number: int):
    con_number: str = str(number)

    left, right = 0, len(con_number) - 1

    while left < right:
        if con_number[left] != con_number[right]:
            return False
        left += 1
        right -= 1

    return True


def find_in_matrix(matrix: list[list[int]], target: int) -> bool:
    for row in range(len(matrix)):
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid == target:
                return True
            elif target < mid:
                right = mid - 1
            elif target > mid:
                left = mid + 1

    return False


def get_platforms(trains: list[list[int]]) -> int:

    max_platforms = 0
    platforms = 1

    for train_number in range(1, len(trains)):
        previous_train = trains[train_number - 1]
        current_train = trains[train_number]

        if current_train[0] < previous_train[1]:
            platforms += 1
        else:
            platforms = 1

        max_platforms = max(platforms, max_platforms)

    return max_platforms
