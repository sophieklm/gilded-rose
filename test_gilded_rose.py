import unittest

from gilded_rose import Item, GildedRose

class GildedRose_NormalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.items = [Item("normal", 5, 10), Item("normal", 0, 10), Item("normal", 0, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_normal_before_sell_date(self):
        self.assertEquals(4, self.items[0].sell_in)
        self.assertEquals(9, self.items[0].quality)

    def test_normal_after_sell_date(self):
        self.assertEquals(-1, self.items[1].sell_in)
        self.assertEquals(8, self.items[1].quality)

    def test_normal_with_zero_quality(self):
        self.assertEquals(-1, self.items[2].sell_in)
        self.assertEquals(0, self.items[2].quality)

class GildedRose_BrieTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.items = [Item("Aged Brie", 5, 10), Item("Aged Brie", 0, 10), Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_brie_before_sell_date(self):
        self.assertEquals(4, self.items[0].sell_in)
        self.assertEquals(11, self.items[0].quality)

    def test_brie_after_sell_date(self):
        self.assertEquals(-1, self.items[1].sell_in)
        self.assertEquals(12, self.items[1].quality)

    def test_brie_with_max_quality(self):
        self.assertEquals(-1, self.items[2].sell_in)
        self.assertEquals(50, self.items[2].quality)

class GildedRose_SulfurasTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.items = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_sulfuras_before_sell_date(self):
        self.assertEquals(5, self.items[0].sell_in)
        self.assertEquals(10, self.items[0].quality)

class GildedRose_BackstagePassTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=49)
            ]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()

    def test_backstage_pass_before_sell_date(self):
        self.assertEquals(14, self.items[0].sell_in)
        self.assertEquals(21, self.items[0].quality)

    def test_backstage_pass_10_days_to_sell_date(self):
        self.assertEquals(9, self.items[1].sell_in)
        self.assertEquals(51, self.items[1].quality)

    def test_backstage_pass_5_days_to_sell_date(self):
        self.assertEquals(4, self.items[2].sell_in)
        self.assertEquals(52, self.items[2].quality)
    
    def test_backstage_pass_after_sell_date(self):
        self.assertEquals(-1, self.items[3].sell_in)
        self.assertEquals(0, self.items[3].quality)

if __name__ == '__main__':
    unittest.main()
