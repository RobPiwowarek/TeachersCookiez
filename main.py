from calculate import calculate_times_for_ranges
import random

if __name__ == '__main__':
    random.seed(None)
    calculate_times_for_ranges([50], [0, 10, 20, 30, 40, 50], [50, 75, 100, 125, 150], [2, 4, 8])
