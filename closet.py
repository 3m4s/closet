
class closet(object):
    def __init__(self, width, height, depth):
        self.width = width          # 衣柜宽度
        self.height = height        # 衣柜高度
        self.depth = depth          # 衣柜深度
        self.grids = {}             # 储物格列表

    # 添加储物格
    def add_grid(self, space):
        if self.space_available(space):
            self.grids[space.name] = space
            return True
        else:
            print("衣柜剩余空间不足！")
            return False
    
    # 删除储物格
    def remove_grid(self, id):
        if id in self.grids:
            del self.grids[id]
            return True
        else:
            print(f"储物格 {id} 不存在！")
            return False

    # 添加衣物到储物格
    def add_item_to_grid(self, id, item):
        if id in self.grids:
            self.grids[id].add_item(item)
            return True
        else:
            print(f"储物格 {id} 不存在！")
            return False

    # 从储物格取出衣物
    def get_item_from_grid(self, id, item_name):
        if id in self.grids:
            self.grids[id].remove_item(item_name)
            return True
        else:
            print(f"储物格 {id} 不存在！")
            return False
    # 查看衣柜是否包含某件衣物
    def contains(self, item_name):
        for grid in self.grids:
            if self.grids[grid].contains(item_name):
                return True
        return False

    def space_available(self, space):
        # 检查衣柜空间是否可用(只考虑体积，不考虑物体形状)
        total_space = self.width * self.height * self.depth
        used_space = sum(i.depth * i.width * i.height for i in self.grids.values())
        item_space = space.depth * space.width * space.height
        return total_space - used_space >= item_space

class grid(object):
    def __init__(self, name, width, height, depth, space_type):
        self.name = name              # 储物格名称
        self.width = width            # 储物格宽度
        self.height = height          # 储物格高度
        self.depth = depth            # 储物格深度
        self.space_type = space_type  # 储物格类型：0-挂放衣物、1-叠放衣物、2-其他用品
        self.items = {}               # 储物格内物品列表
        self.space_type_name = {0:"挂放衣物", 1:"叠放衣物", 2:"其他物品"}

    def add_item(self, item):
        if self.space_type == item.item_type:
            if self.space_available(item):
                self.items[item.name] = item
                return True
            else:
                print("储物格已满，无法添加物品！")
                return False
        else:
            print(f"{self.name}只能放{self.space_type_name[self.space_type]}")
            return False

    def remove_item(self, item_name):
        if item in self.items:
            del self.items[item_name]
            return True
        else:
            print("物品不存在于该储物格中！")
            return False
        
    def contains(self, item_name):
        if item_name in self.items:
            return True
        else:
            return False

    def space_available(self, item):
        # 检查储物格空间是否可用(只考虑体积，不考虑物体形状)
        total_space = self.width * self.height * self.depth
        used_space = sum(i.depth * i.width * i.height for i in self.items.values())
        item_space = item.depth * item.width * item.height
        return total_space - used_space >= item_space
    
class item(object):
    def __init__(self):
        self.name       # 物品名称
        self.width      # 物品宽度
        self.height     # 物品高度
        self.depth      # 物品长度(深度)
        self.item_type  # 物品类型：0-挂放衣物、1-叠放衣物、2-其他物品

class clothe(item):
    def __init__(self, name, width, height, depth, item_type = 0):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.item_type = item_type
    # 折叠衣服
    def fold_clothe(self):
        self.item_type = 1
    # 展开衣服
    def expand_clothe(self):
        self.item_type = 0

class pant(item):
    def __init__(self, name, width, height, depth, item_type = 1):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.item_type = item_type
    # 折叠裤子
    def fold_clothe(self):
        self.item_type = 1
    # 展开裤子
    def expand_clothe(self):
        self.item_type = 0

class other(item):
    def __init__(self, name, width, height, depth, item_type = 2):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.item_type = item_type

if __name__=='__main__':
    closet = closet(100, 200, 40)
    closet.add_grid(grid("格子0",50,50,40,0))
    closet.add_grid(grid("格子1",50,50,40,1))
    closet.add_grid(grid("格子2",50,50,40,2))
    closet.add_item_to_grid("格子0", clothe("衣服1",10,10,20))
    closet.add_item_to_grid("格子1", pant("裤子1",10,10,20))
    closet.add_item_to_grid("格子2", other("化妆品",10,10,10))
    closet.add_item_to_grid("格子3", other("化妆品",10,10,10))