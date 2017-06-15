class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "Aged Brie" in item.name:
                item.brie_update()
            elif "Sulfuras" in item.name:
                return
            elif "Backstage passes" in item.name:
                item.backstage_pass_update()
            elif "Conjured" in item.name:
                item.conjured_update()
            else:
                item.normal_update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def normal_update(self):
        self.sell_in -= 1
        if self.quality == 0:
            return
        self.quality -= 1
        if self.sell_in <= 0:
            self.quality -= 1

    def brie_update(self):
        self.sell_in -= 1
        if self.quality >= 50:
            return
        self.quality += 1
        if self.sell_in <= 0:
            self.quality += 1

    def backstage_pass_update(self):
        self.sell_in -= 1
        if self.quality == 0 or self.quality == 50:
            return
        self.quality += 1
        if self.sell_in <= 0:
            self.quality = 0
            return
        if self.quality < 50:
            if self.sell_in <= 10:
                self.quality += 1
            if self.sell_in <= 5:
                self.quality += 1

    def conjured_update(self):
        self.sell_in -= 1
        if self.quality == 0:
            return
        self.quality -= 2
        if self.sell_in <= 0:
            self.quality -= 2

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
