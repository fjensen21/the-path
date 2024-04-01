# importing libraries
from collections import Counter
import heapq


def reorganize_string(str):
    character_freq = Counter(str)
    max_heap = []
    output = ""
    prev = None

    for char, freq in character_freq.items():
        heapq.heappush(max_heap, (-freq, char))

    while max_heap:
        freq, char = heapq.heappop(max_heap)
        output += char
        freq += 1

        if prev:
            heapq.heappush(max_heap, prev)
            prev = None

        if freq < 0:
            prev = (freq, char)

    if prev:
        return ""

    return output


if __name__ == "__main__":
    print(reorganize_string("abb"))
