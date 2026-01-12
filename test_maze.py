from maze import Maze
from astar import astar_search

def test_maze(file):
    maze = Maze(file)
    path = astar_search(maze)
    return path

if __name__ == "__main__":
    for m in ["data/maze1.txt", "data/maze2.txt"]:
        result = test_maze(m)
        print(m, "=>", "Path Found" if result else "No Path")
