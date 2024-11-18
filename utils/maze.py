from pyamaze import maze, agent, COLOR

# Create a maze
m = maze(50, 50)
m.CreateMaze()

# Add an agent
a = agent(m, filled=True, footprints=True)

# Solve and display the maze
m.tracePath({a: m.path})
m.run()
