map = open('input').read().split('\n')[:-1]

map_length = len(map[0])
map_height = len(map)

slopes = [
    {'x': 1, 'y': 1},
    {'x': 3, 'y': 1},
    {'x': 5, 'y': 1},
    {'x': 7, 'y': 1},
    {'x': 1, 'y': 2}
]


def point_at_location(location):
    return map[location['y']][location['x'] % map_length]


def get_tree_collision_from_slope(slope):
    current_location = {'x': 0, 'y': 0}
    collisions = 0
    while current_location['y'] < map_height:
        if point_at_location(current_location) == '#':
            collisions += 1
        current_location['x'] += slope['x']
        current_location['y'] += slope['y']
    return collisions


print(f'Part 1 solution: {get_tree_collision_from_slope(slopes[1])}')

# Part 2
slope_collisions = [get_tree_collision_from_slope(slope) for slope in slopes]
collisions_multiplied = 1
for i in slope_collisions:
    collisions_multiplied *= i

print(f'Part 2 solution: {collisions_multiplied}')
