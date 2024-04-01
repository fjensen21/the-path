from heapq import heappush, heappop
from collections import defaultdict


class MedianFinder:
    def __init__(self):
        self.max_of_smallest = []
        self.min_of_largest = []
        self.balance = 0
        self.lazy_removal = defaultdict(int)

    def add(self, num):
        if not self.max_of_smallest or num <= -self.max_of_smallest[0]:
            heappush(self.max_of_smallest, -num)
            self.balance -= 1
        else:
            heappush(self.min_of_largest, num)
            self.balance += 1

        self.rebalance()
    def remove(self, num):
        self.lazy_removal[num] += 1
        if num <= -self.max_of_smallest[0]:
            self.balance += 1
        else:
            self.balance -= 1

        self.rebalance()
        self.lazy_remove()

    def find_median(self):
        if self.balance == 0:
            return (-self.max_of_smallest[0] + self.min_of_largest[0]) / 2.0
        elif self.balance < 0:
            return -self.max_of_smallest[0]
        else:
            return self.min_of_largest[0]

    def rebalance(self):
        while self.balance < 0:
            heappush(self.min_of_largest, -heappop(self.max_of_smallest))
            self.balance += 2

        while self.balance > 0:
            heappush(self.max_of_smallest, -heappop(self.min_of_largest))
            self.balance -= 2

    def lazy_remove(self):
        while self.max_of_smallest and self.lazy_removal[-self.max_of_smallest[0]] > 0:
            self.lazy_removal[-self.max_of_smallest[0]] -= 1
            heappop(self.max_of_smallest)

        while self.min_of_largest and self.lazy_removal[self.min_of_largest[0]] > 0:
            self.lazy_removal[self.min_of_largest[0]] -= 1
            heappop(self.min_of_largest)


def median_sliding_window(nums, k):
    median_finder = MedianFinder()
    result = []

    for i, num in enumerate(nums):
        median_finder.add(num)

        if i >= k:
            median_finder.remove(nums[i - k])

        if i >= k - 1:
            result.append(median_finder.find_median())

    return result
