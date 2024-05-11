from time import time


def print2D(root):
    COUNT = [10]

    def print2DUtil(root, space):
        # Base case
        if root == None:
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for _ in range(COUNT[0], space):
            print(end=" ")
        print(root.value)

        # Process left child
        print2DUtil(root.left, space)

    # Pass initial space count as 0
    print2DUtil(root, 0)


def time_it(func, *args, **kwargs) -> None:
    start: float = time()
    func(*args, **kwargs)
    end: float = time()
    print(f"Time taken: {end - start:.10f}s")
