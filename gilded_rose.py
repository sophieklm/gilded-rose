class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.brie_update_quality(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.sulfuras_update_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.backstage_pass_update_quality(item)
            elif item.name == "Conjured Mana Cake":
                self.conjured_update_quality(item)
            else:
                self.normal_update_quality(item)

    def normal_update_quality(self, item):
        item.sell_in -= 1
        if item.quality == 0:
            return
        item.quality -= 1
        if item.sell_in <= 0:
            item.quality -= 1

    def brie_update_quality(self, item):
        item.sell_in -= 1
        if item.quality >= 50:
            return
        item.quality += 1
        if item.sell_in <= 0:
            item.quality += 1

    def sulfuras_update_quality(self, item):
        item.sell_in
        item.quality

    def backstage_pass_update_quality(self, item):
        item.sell_in -= 1
        if item.quality == 0 or item.quality == 50:
            return
        item.quality += 1
        if item.sell_in <= 0:
            item.quality = 0
        if item.quality < 50:
            if item.sell_in <= 10:
                item.quality += 1
            if item.sell_in <= 5:
                item.quality += 1
            if item.sell_in <= 0:
                item.quality = 0

    def conjured_update_quality(self, item):
        item.sell_in -= 1
        if item.quality == 0:
            return
        item.quality -= 2
        if item.sell_in <= 0:
            item.quality -= 2

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
