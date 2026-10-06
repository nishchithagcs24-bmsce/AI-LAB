import heapq


GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)      



def manhattan_distance(state):
    distance = 0

    for i in range(9):
        tile = state[i]

    
        if tile == 0:
            continue

       
        current_row = i // 3
        current_col = i % 3

  
        goal_index = GOAL.index(tile)
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance



def get_successors(state):
    successors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        ("UP", -1, 0),
        ("DOWN", 1, 0),
        ("LEFT", 0, -1),
        ("RIGHT", 0, 1)
    ]

    for action, dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank and tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            successors.append((tuple(new_state), action))

    return successors



def display(state):
    for i in range(0, 9, 3):
        print(
            " ".join(
                "_" if x == 0 else str(x)
                for x in state[i:i + 3]
            )
        )
    print()



def a_star(start):

  
    g = 0


    h = manhattan_distance(start)

 
    f = g + h

 
    frontier = []

    heapq.heappush(
        frontier,
        (f, g, start, [])
    )

    explored = set()

    while frontier:

        f, g, state, path = heapq.heappop(frontier)

       
        if state == GOAL:
            return path + [(state, None)]

     
        if state in explored:
            continue

        explored.add(state)

        for child, action in get_successors(state):

            if child not in explored:

                new_g = g + 1
                new_h = manhattan_distance(child)
                new_f = new_g + new_h

                new_path = path + [(state, action)]

                heapq.heappush(
                    frontier,
                    (new_f, new_g, child, new_path)
                )

    return None




print("Enter the initial 8-puzzle configuration")
print("Use _ for the blank position.")

state = []

for i in range(3):
    row = input().split()

    for value in row:
        if value == "_":
            state.append(0)
        else:
            state.append(int(value))

start = tuple(state)

print("\nInitial State:")
display(start)


solution = a_star(start)

if solution is None:

    print("No solution exists.")

else:

    move_number = 0

    for state, action in solution:

        if action is not None:
            move_number += 1
            print("Move", move_number, ":", action)

        display(state)

    print("Goal State Reached")
    print("Solution Cost =", move_number)
