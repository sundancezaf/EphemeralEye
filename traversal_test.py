import os

# traverse root directory, and list directories as dirs and files as files


def dir_traversal():
    for root, dirs, files in os.walk("."):
        print(root)
        path = root.split(os.sep)
        # print((len(path) - 1) * "---", os.path.basename(root))
        # print(path)
    # for file in files:
    # print(len(path) * "---", file)


dir_traversal()
