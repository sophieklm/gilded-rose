def normal_update(item):
    item.sell_in -= 1
    if item.quality == 0:
        return
    item.quality -= 1
    if item.sell_in <= 0:
        item.quality -= 1

def brie_update(item):
    item.sell_in -= 1
    if item.quality >= 50:
        return
    item.quality += 1
    if item.sell_in <= 0:
        item.quality += 1

def backstage_update(item):
    item.sell_in -= 1
    if item.quality == 0 or item.quality == 50:
        return
    item.quality += 1
    if item.sell_in <= 0:
        item.quality = 0
        return
    if item.quality < 50:
        if item.sell_in <= 10:
            item.quality += 1
        if item.sell_in <= 5:
            item.quality += 1

def conjured_update(item):
    item.sell_in -= 1
    if item.quality == 0:
        return
    item.quality -= 2
    if item.sell_in <= 0:
        item.quality -= 2

def sulfuras_update(item):
    return

class GildedRose(object):

    TYPE = {
        "Aged Brie": brie_update,
        "Sulfuras, Hand of Ragnaros": sulfuras_update,
        "Backstage passes to a TAFKAL80ETC concert": backstage_update,
        "Conjured Mana Cake": conjured_update
    }

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            try:
                self.TYPE[item.name](item)
            except KeyError:
                normal_update(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
