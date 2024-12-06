import random

# Define All States
states = {"Start", "Stop", "Slow Down", "Forward", "Turn", "Stop-End Trip", "Avoid Obstacle"}

# Initialize Percepts
light = {'red': 0, 'green': 0, 'yellow': 0}
dist_to_light = {'near': 0, 'far': 0}
destination_reached = {'y': 0, 'n': 0}
front_car = {'near': 0, 'far': 0, 'stopped': 0}
gps_command = {'right': 0, 'left': 0, 'u-turn': 0, 'none': 0}
intersection = {'yes': 0, 'no': 0}

# LiDAR readings (simulated grid)
grid_size = 10
obstacle_positions = set()
agent_position = [0, 0]
destination = [9, 9]

# State Initialization
state = 'Start'
max_steps = 1000  # Maximum steps before stopping
current_step = 0

print('Initial State =', state)

# Helper Functions
def simulate_lidar():
    """Simulates LiDAR readings in a grid environment."""
    global obstacle_positions
    obstacle_positions = {(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(5)}
    print("LiDAR detected obstacles at:", obstacle_positions)

def move_agent(action):
    """Moves the agent in the grid."""
    if action == "Forward":
        agent_position[1] = min(agent_position[1] + 1, grid_size - 1)  # Move up
    elif action == "Turn Right":
        agent_position[0] = min(agent_position[0] + 1, grid_size - 1)  # Move right
    elif action == "Turn Left":
        agent_position[0] = max(agent_position[0] - 1, 0)  # Move left
    elif action == "U-Turn":
        agent_position[1] = max(agent_position[1] - 1, 0)  # Move down
    print("Agent moved to:", agent_position)

def check_obstacle():
    """Checks if there's an obstacle in the agent's path."""
    return tuple(agent_position) in obstacle_positions

# Start Navigation
while current_step < max_steps:
    current_step += 1  # Increment step counter
    print(f"\nStep: {current_step}")

    # Simulate environment changes
    simulate_lidar()
    obstacle_nearby = check_obstacle()
    destination_reached_flag = agent_position == destination

    # FSM Logic
    print("==================================")
    if state == 'Start':
        if obstacle_nearby:
            state = 'Avoid Obstacle'
        else:
            state = 'Forward'
    elif state == 'Stop':
        if destination_reached_flag:
            state = 'Stop-End Trip'
        elif not obstacle_nearby:
            state = 'Forward'
    elif state == 'Slow Down':
        if destination_reached_flag:
            state = 'Stop-End Trip'
        elif obstacle_nearby:
            state = 'Avoid Obstacle'
        else:
            state = 'Forward'
    elif state == 'Forward':
        if destination_reached_flag:
            state = 'Stop-End Trip'
        elif obstacle_nearby:
            state = 'Avoid Obstacle'
        elif random.choice([True, False]):  # Simulate intersections
            state = 'Turn'
        else:
            move_agent("Forward")
    elif state == 'Turn':
        gps_action = random.choice(['right', 'left', 'u-turn'])
        if gps_action == 'right':
            print("Turning Right...")
            move_agent("Turn Right")
        elif gps_action == 'left':
            print("Turning Left...")
            move_agent("Turn Left")
        elif gps_action == 'u-turn':
            print("Making a U-Turn...")
            move_agent("U-Turn")
        state = 'Forward'
    elif state == 'Avoid Obstacle':
        print("Obstacle detected! Calculating new path...")
        # Implement basic avoidance (e.g., move around the obstacle)
        move_agent(random.choice(["Turn Left", "Turn Right"]))
        state = 'Forward'
    elif state == 'Stop-End Trip':
        print('Destination Reached! Trip Ended!')
        break
    else:
        print("ERROR: Unknown State!!!")
        break

    # Adding state output
    print(f"State changed to: {state}")

# Check why the loop ended
if current_step >= max_steps:
    print("Maximum steps reached. Stopping the program.")
elif state == 'Stop-End Trip':
    print("Program terminated successfully after reaching the destination.")
