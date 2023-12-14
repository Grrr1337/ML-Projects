import math
import statistics

def calculate_median(numbers):
    # Calculate the median manually
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]

def print_statistics_summary(variable_name, numbers):
    print(f"\nVariable name: {variable_name}")
    print(f"Mean value: {statistics.mean(numbers)}")
    print(f"Std deviation: {statistics.stdev(numbers)}")
    print(f"pvariance: {statistics.pvariance(numbers)}")
    print(f"pstdev: {statistics.pstdev(numbers)}")
    print(f"Harmonic mean: {statistics.harmonic_mean(numbers) if all(x != 0 for x in numbers) else 0:.4f}")

def main():
    # Test data
    numbers1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    numbers2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1000]
    numbers3 = [10, 10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100000, 200000]
    numbers4 = [0, 1, 2, 3, 10000, 20000, 30000]
    numbers5 = [8500, 8550, 8580, 8600]

    # Perform tests
    print("\nTest 1:")
    print(f"Mean value: {sum(numbers3) / len(numbers3)}")
    print(f"Mean value: {statistics.mean(numbers3)}")
    print(f"Median value: {statistics.median(numbers3)}")
    print(f"Mode: {statistics.mode(numbers3)}")
    print(f"Manual Median: {calculate_median(numbers3)}")
    print(f"Mode (manual): {max(set(numbers3), key=numbers3.count)}")
    print(f"Median_high: {statistics.median_high(numbers3)}")
    print(f"Median_low: {statistics.median_low(numbers3)}")

    print("\nTest 2:")
    print(f"Mean value: {statistics.mean(numbers5)}")
    print(f"Standard deviation: {statistics.stdev(numbers5)}")
    print(f"pvariance: {statistics.pvariance(numbers4)}")
    print(f"pstdev: {statistics.pstdev(numbers4)}")
    print(f"Harmonic mean: {statistics.harmonic_mean(numbers4)}")

    print("\nTest 3 (GPT-ed):")
    variables = {
        "numbers1": numbers4,
        "numbers2": numbers5,
        "numbers3": [1, 2, 3, 10000, 20000, 3_000_000_000_000],
    }

    for name, values in variables.items():
        print_statistics_summary(name, values)

if __name__ == '__main__':
    main()
