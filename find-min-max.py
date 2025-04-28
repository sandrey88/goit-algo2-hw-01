def find_min_max(arr):
    def helper(left, right):
        # Базовий випадок: один елемент
        if left == right:
            return arr[left], arr[left]
        # Базовий випадок: два елементи
        if right - left == 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]
        # Рекурсивний випадок: розділяємо масив навпіл
        mid = (left + right) // 2
        min1, max1 = helper(left, mid)
        min2, max2 = helper(mid + 1, right)
        return min(min1, min2), max(max1, max2)

    if not arr:
        raise ValueError("Масив не повинен бути порожнім")
    return helper(0, len(arr) - 1)

if __name__ == "__main__":
    test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [42],
        [7, -3],
        [5, 5, 5, 5],
        []
    ]

    for idx, arr in enumerate(test_arrays, 1):
        print(f"Тест {idx}: масив = {arr}")
        try:
            min_val, max_val = find_min_max(arr)
            print(f"  Мінімум: {min_val}, Максимум: {max_val}\n")
        except ValueError as e:
            print(f"  Помилка: {e}\n")