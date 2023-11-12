def find_fastest_path(universe_count, portal_count, travel_times, demon_patrols):
    shortest_times = [float('inf')] * universe_count
    shortest_times[0] = 0
    demon_influence = 0
    
    for source_universe in range(universe_count):
        for destination_universe in range(universe_count):
            if travel_times[source_universe][destination_universe] != -1:
                if shortest_times[source_universe] + travel_times[source_universe][destination_universe] in demon_patrols[destination_universe]:
                    demon_influence = 1
                else:
                    demon_influence = 0
                if shortest_times[destination_universe] > shortest_times[source_universe] + demon_influence + travel_times[source_universe][destination_universe]:
                    shortest_times[destination_universe] = shortest_times[source_universe] + demon_influence + travel_times[source_universe][destination_universe]
   
    if shortest_times[universe_count - 1] != float('inf'):
        return shortest_times[universe_count - 1]
    else:
        return -1

if __name__ == '__main__':
    universe_count, portal_count = map(int, input().split())
    travel_times = [[-1] * universe_count for _ in range(universe_count)]
   
    for _ in range(portal_count):
        source_universe, destination_universe, travel_time = map(int, input().split())
        travel_times[source_universe - 1][destination_universe - 1] = travel_time
   
    demon_patrols = []
    for _ in range(universe_count):
        patrol_info = set(input().split())
        demon_patrols.append(patrol_info)
    
    shortest_time = find_fastest_path(universe_count, portal_count, travel_times, demon_patrols)
    print(shortest_time)
