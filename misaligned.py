
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    colorMap = list()
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            colorMap.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors), colorMap


result, colorMap = print_color_map()
assert(result == 25)
assert(len(colorMap[0]) == len(colorMap[-1])), "Incorrect alignment"
assert(len(colorMap[0].split('|')[0])  == len(colorMap[-1].split('|')[0])), "Incorrect alignment"
print("All is well (maybe!)\n")
