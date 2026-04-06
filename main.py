import time
import random
import bisect


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def binary_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        pos = bisect.bisect_right(arr, val, 0, i)
        arr.insert(pos, arr.pop(i))
    return arr


if __name__ == "__main__":
    # Демонстрація для звіту (20 випадкових значень)
    demo_data = [random.randint(1, 100) for _ in range(20)]
    print("Початковий масив (20 значень):")
    print(*(demo_data))

    sorted_demo = bubble_sort(demo_data.copy())
    print("\nВідсортований масив (20 значень):")
    print(*(sorted_demo))

    # Замір часу (10 000 значень)
    large_data = [random.randint(1, 100000) for _ in range(10000)]

    start = time.time()
    bubble_sort(large_data.copy())
    print(f"\nЧас Bubble Sort (10k): {time.time() - start:.4f} сек")

    start = time.time()
    binary_sort(large_data.copy())
    print(f"Час Binary Sort (10k): {time.time() - start:.4f} сек")