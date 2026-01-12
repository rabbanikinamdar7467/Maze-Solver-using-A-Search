from maze import Maze
from astar import astar_search
from visualization import visualize

def run(file):
    maze = Maze(file)
    path = astar_search(maze)

    if path:
        print("Path Found:", path)
    else:
        print("No Path Found")

    visualize(maze, path, title=f"A* Solver | {file}")

if __name__ == "__main__":
    run("data/maze1.txt")
    run("data/maze2.txt")
