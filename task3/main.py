def merge_intervals(intervals: list[int]) -> list[list[int]]:
    """Объединяет пересекающиеся интервалы."""
    intervals = sorted(zip(intervals[::2], intervals[1::2]))
    merged = []
    for start, end in intervals:
        if merged and merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

def intersect_intervals(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Находит пересечение двух списков интервалов."""
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        start, end = max(a[i][0], b[j][0]), min(a[i][1], b[j][1])
        if start < end:
            result.append([start, end])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result

def appearance(intervals: dict[str, list[int]]) -> int:
    """Вычисляет общее время пересечения интервалов ученика, учителя и урока."""
    lesson = merge_intervals(intervals['lesson'])
    pupil = merge_intervals(intervals['pupil'])
    tutor = merge_intervals(intervals['tutor'])

    # Находим пересечение интервалов
    common_intervals = intersect_intervals(pupil, tutor)
    final_intervals = intersect_intervals(common_intervals, lesson)

    # Результат - сумма получившихся
    return sum(end - start for start, end in final_intervals)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'