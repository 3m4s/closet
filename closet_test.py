import unittest

from closet import closet, grid, clothe, pant, other

class TestStoreObjectInEmptyCloset(unittest.TestCase):

    closet = None

    def setUp(self):
        # super.setUp()
        # 初始化衣柜对象
        self.closet = closet(100, 200, 40)
        # 添加储物格
        self.closet.add_grid(grid("格子0",50,50,40,0))
        self.closet.add_grid(grid("格子1",50,50,40,1))
        self.closet.add_grid(grid("格子2",50,50,40,2))
        print("Closet init done.")

    def test_store_object(self):
        # 放入衣物
        self.closet.add_item_to_grid("格子0", clothe("衣服1",10,10,20))
        self.closet.add_item_to_grid("格子1", pant("裤子1",10,10,20))
        self.closet.add_item_to_grid("格子2", other("化妆品",10,10,10))
        # 判断是否正确放入
        self.assertTrue(self.closet.contains("衣服1"))
        self.assertTrue(self.closet.contains("裤子1"))
        self.assertTrue(self.closet.contains("化妆品"))
    
    def tearDown(self):
        # super.tearDown()
        # 移除储物格
        self.closet.remove_grid("格子0")
        self.closet.remove_grid("格子1")
        self.closet.remove_grid("格子2")
        print("Closet finish done.")

if __name__ == '__main__':
    unittest.main()
