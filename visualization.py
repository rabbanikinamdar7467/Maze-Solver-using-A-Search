import matplotlib.pyplot as plt
import numpy as np

def visualize(maze, path, title="A* Maze Solver"):
    grid = np.array(maze.grid)

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("#020617")
    ax.set_facecolor("#020617")

    ax.imshow(grid, cmap="gray_r")

    if path:
        y, x = zip(*path)
        ax.plot(x, y, color="#22d3ee", linewidth=4, label="Optimal Path")

    ax.scatter(maze.start[1], maze.start[0],
               c="#22c55e", s=250, marker="o", label="Start")
    ax.scatter(maze.goal[1], maze.goal[0],
               c="#ef4444", s=250, marker="X", label="Goal")

    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(facecolor="#020617", edgecolor="white", labelcolor="white")

    plt.title(title, color="white", fontsize=14)
    plt.show()
