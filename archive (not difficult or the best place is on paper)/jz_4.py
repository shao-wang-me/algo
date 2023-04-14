import random
import timeit
import functools


def is_empty_matrix(matrix):
    """看输入是否有效或超出范围"""
    if not matrix or not matrix[0]:
        return True
    return False


def is_out_of_range(matrix, target):
    """看target是否超出matrix范围"""
    smallest = matrix[0][0]
    largest = matrix[-1][-1]
    if target < smallest or target > largest:
        return True
    return False


def f1(matrix, target, out_of_range_check=False):
    """一个个看，O(mn)"""
    if is_empty_matrix(matrix):
        return False
    if out_of_range_check and is_out_of_range(matrix, target):
        return False
    for row in matrix:
        for number in row:
            if number == target:
                return True
    return False


def f2(matrix, target, out_of_range_check=False):
    """逐行二分法，O(min(mlogn, nlogm))"""
    if is_empty_matrix(matrix):
        return False
    if out_of_range_check and is_out_of_range(matrix, target):
        return False
    
    pass


def f3(matrix, target, out_of_range_check=False):
    """正解：每次消一行或一列，O(m + n)"""
    if is_empty_matrix(matrix):
        return False
    if out_of_range_check and is_out_of_range(matrix, target):
        return False
    pass


def f4(matrix, target, out_of_range_check=False):
    """每次既看行，又看列，元素逐个看"""
    if is_empty_matrix(matrix):
        return False
    if out_of_range_check and is_out_of_range(matrix, target):
        return False
    pass


def f5(matrix, target, out_of_range_check=False):
    """每次既看行，又看列，且用二分法看"""
    if is_empty_matrix(matrix):
        return False
    if out_of_range_check and is_out_of_range(matrix, target):
        return False
    pass


class TestCaseGenerator:
    IN_MATRIX = 1
    NOT_IN_MATRIX_BUT_WITHIN_RANGE = 2
    SMALLER_THAN_RANGE = 3
    LARGER_THAN_RANGE = 4

    @functools.cache
    @staticmethod
    def generate_matrix(rows, columns, scale=1):
        scale = int(scale)
        matrix = [[0] * columns for _ in range(rows)]
        random.seed(12)
        for i in range(rows):
            for j in range(columns):
                if not i == j == 0:
                    min_int = max(
                        matrix[max(0, i - 1)][j],
                        matrix[i][max(0, j - 1)])
                    matrix[i][j] = min_int + random.randint(0, 10) * scale
        return matrix

    @classmethod
    def generate_data(cls, rows, columns, target_type, scale=1):
        """生成数据"""
        matrix = cls.generate_matrix(rows, columns, scale)
        random.seed(12)
        target = None
        if target_type == cls.IN_MATRIX:
            target = random.choice(random.choice(matrix))
        elif target_type == cls.NOT_IN_MATRIX_BUT_WITHIN_RANGE:
            def is_in_matrix(matrix, target):
                for row in matrix:
                    for integer in row:
                        if target == integer:
                            return True
                return False
            max_int = matrix[-1][-1]
            target = random.randint(0, max_int)
            while is_in_matrix(matrix, target):
                target = random.randint(0, max_int)
        elif target_type == cls.SMALLER_THAN_RANGE:
            target = random.randint(-1000, -1)
        elif target_type == cls.LARGER_THAN_RANGE:
            target = random.randint(1, 1000) + matrix[-1][-1]
        print('数据生成完毕')
        return matrix, target, target_type == cls.IN_MATRIX


def pprint_matrix(matrix, indent=0):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    table = [' ' * indent + x for x in table]
    print('\n'.join(table))


def main():
    test_cases = [
        ([], 5, False),  # 测试用例1
        ([[]], 5, False),  # 测试用例2
        TestCaseGenerator.generate_data(5, 10, TestCaseGenerator.IN_MATRIX),  # 测试用例3
        TestCaseGenerator.generate_data(5, 10, TestCaseGenerator.NOT_IN_MATRIX_BUT_WITHIN_RANGE),  # 测试用例4
        TestCaseGenerator.generate_data(5, 10, TestCaseGenerator.SMALLER_THAN_RANGE),  # 测试用例5
        TestCaseGenerator.generate_data(5, 10, TestCaseGenerator.LARGER_THAN_RANGE),  # 测试用例6
        TestCaseGenerator.generate_data(10000, 1000, TestCaseGenerator.IN_MATRIX),  # 测试用例7
        TestCaseGenerator.generate_data(10000, 1000, TestCaseGenerator.NOT_IN_MATRIX_BUT_WITHIN_RANGE),  # 测试用例8
        TestCaseGenerator.generate_data(10000, 1000, TestCaseGenerator.SMALLER_THAN_RANGE),  # 测试用例9
        TestCaseGenerator.generate_data(10000, 1000, TestCaseGenerator.LARGER_THAN_RANGE)  # 测试用例10
    ]
    for i, (matrix, target, expected_result) in enumerate(test_cases):
        print(f'=== 测试用例{i + 1}:')
        print('  矩阵：')
        # pprint_matrix(matrix, 2)
        print(f'  目标：{target}')
        print(f'  答案：{expected_result}')
        for f in [f1]:
            def function_1():
                return f(matrix, target)

            def function_2():
                return f(matrix, target, True)
            print(f'  --- 函数：{f.__name__}')
            result_1 = function_1()
            result_2 = function_2()
            print(f'    无值域检查结果：{result_1}, {"对" if result_1 == expected_result else "错"}！')
            print(f'    有值域检查结果：{result_2}, {"对" if result_2 == expected_result else "错"}！')
            # print(f'    无值域检查用时：{timeit.timeit(function_1)}')
            # print(f'    有值域检查用时：{timeit.timeit(function_2)}')


if __name__ == '__main__':
    main()
