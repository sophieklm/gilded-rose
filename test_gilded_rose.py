import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_normal_before_sell_date(self):
        items = [Item("normal", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.normal_update_quality()
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(9, items[0].quality)

    def test_normal_after_sell_date(self):
        items = [Item("normal", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.normal_update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(8, items[0].quality)

    def test_normal_with_zero_quality(self):
        items = [Item("normal", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.normal_update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
