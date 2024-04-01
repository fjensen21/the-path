from collections import defaultdict, deque


def minimum_buses(bus_routes, src, dest):
    buses_from_station = defaultdict(list)
    visited = set()

    for i, route in enumerate(bus_routes):
        for station in route:
            buses_from_station[station].append(i)

    queue = deque([[src, 0]])

    while queue:
        station, buses_taken = queue.pop()
        if dest == station:
            return buses_taken

        for bus in buses_from_station[station]:
            for next_station in bus_routes[bus]:
                if next_station not in visited:
                    visited.add(next_station)
                    queue.appendleft([next_station, buses_taken + 1])

    return -1
