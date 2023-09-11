
import json

def find_depth(data):
    parent_child_dict = {}
    
    for child, parent in data:
        parent_child_dict[child] = parent

    def get_depth(node):
        depth = 0
        while node in parent_child_dict:
            node = parent_child_dict[node]
            depth += 1
        return depth - 1
    
    depth_of_children_dict = {}
    
    for child, parent in data:
        depth = get_depth(child)
        if depth not in depth_of_children_dict:
            depth_of_children_dict[depth] = []
        depth_of_children_dict[depth].append(child)
    
    return depth_of_children_dict

f = open('parse.json')
data = json.load(f)
c_p = []

for i in range(len(data[0]['events'])):
    c_p.append([data[0]['events'][i][1],(data[0]['events'][i][9][0].split(',')[1][8:])])

depth_children = find_depth(c_p)
print("Depth of Tree : ", len(depth_children))

for depth, children in sorted(depth_children.items()):
    print(f"{depth}: {children}")

f.close()