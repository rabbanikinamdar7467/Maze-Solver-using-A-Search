class Maze:
    def __init__(self, file_path):
        self.grid = []
        self.start = None
        self.goal = None
        self._load(file_path)

    def _load(self, file_path):
        with open(file_path) as f:
            for r, line in enumerate(f):
                row = line.strip().split()
                for c, val in enumerate(row):
                    if val == "S":
                        self.start = (r, c)
                        row[c] = 0
                    elif val == "G":
                        self.goal = (r, c)
                        row[c] = 0
                self.grid.append(list(map(int, row)))

    def is_valid(self, node):
        r, c = node
        return (
            0 <= r < len(self.grid) and
            0 <= c < len(self.grid[0]) and
            self.grid[r][c] == 0
        )
