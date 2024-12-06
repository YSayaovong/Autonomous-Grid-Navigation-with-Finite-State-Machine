# Autonomous Grid Navigation with Finite State Machine

This project is a Python-based simulation that demonstrates an autonomous navigation system using a Finite State Machine (FSM). The agent navigates a grid environment, intelligently handling obstacles, intersections, and destination detection.

## Features

- **Finite State Machine Logic**:
  - States include: `Start`, `Stop`, `Slow Down`, `Forward`, `Turn`, `Avoid Obstacle`, and `Stop-End Trip`.
  - Dynamic state transitions based on environmental inputs.

- **Obstacle Detection and Avoidance**:
  - Simulated LiDAR sensors detect obstacles within the grid.
  - The agent recalculates its path to avoid collisions.

- **Grid Navigation**:
  - Agent starts at a predefined location and navigates toward a destination in a 10x10 grid.

- **Randomized Environment**:
  - Obstacle positions and GPS commands are randomly generated to simulate real-world unpredictability.

## How It Works

1. **Initialize Environment**:
   - The grid environment is set up with random obstacle placements.
   - The agent is initialized at a starting point with a target destination.

2. **State Transition Logic**:
   - The FSM transitions between states based on:
     - Obstacle proximity.
     - Reaching the destination.
     - GPS commands for turning.

3. **Simulation Steps**:
   - Each step updates the agent’s position, checks for obstacles, and determines the next state.

4. **End of Simulation**:
   - The simulation terminates when the agent reaches the destination or a maximum step limit is reached.
