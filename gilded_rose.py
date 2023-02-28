class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

#Assumptions for the the code 
#1. Item quality cant be less than 0 (Even when passed)
#2. Item quality cant be more than 50 (Even when passed)
#3. Item quality for Sulfuras is 80

#Tests from the original code that failed, from the description that was given in the requirements
#Conjured items dont exist in existing code, so 4th test failed as the functionality wasnt implemented yet
# ========================= short test summary info ==========================
# FAILED test_gilded_rose.py::test_normal_item_quality_is_never_negitive_even_when_passed - assert -1 == 0
# FAILED test_gilded_rose.py::test_normal_item_quality_cant_be_more_than_50_even_when_passed - assert 54 == 50
# FAILED test_gilded_rose.py::test_sulfuras_quality_is_80 - assert 40 == 80
# FAILED test_gilded_rose.py::test_conjured_item_degrades_twice_as_fast_as_normal_item - assert 19 == 18
# ======================= 4 failed, 9 passed in 0.03s ========================

class GildedRose:
    def __init__(self, items:list[Item]):
        self.items = items
        self.max_quality = 50 
        self.min_quality = 0

    def update_max_qualilty(self, max_quality:int) -> None:
        self.max_quality = max_quality

    def update_min_qualilty(self, min_quality:int) -> None:
        self.min_quality = min_quality

    def update_quality(self) -> None:
        for item in self.items:
            self.update_item(item)

    def update_item(self, item:Item) -> None:
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            self.update_sulfuras(item)
        elif item.name == "Conjured":
            self.update_conjured(item)
        else:
            self.update_normal_item(item)

    def update_normal_item(self, item:Item) -> None:
        item.sell_in -= 1
        item.quality -= 2 if item.sell_in < 0 else 1
        item.quality = max(item.quality, self.min_quality) if item.quality < 0 else min(item.quality, self.max_quality)
        
    def update_aged_brie(self, item:Item) -> None:
        item.sell_in -= 1
        item.quality += 2 if item.sell_in < 0 else 1
        item.quality = max(item.quality, self.min_quality) if item.quality < 0 else min(item.quality, self.max_quality)

    def update_backstage_pass(self, item:Item) -> None:
        item.sell_in -= 1
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = max(item.quality, self.min_quality) if item.quality < 0 else min(item.quality, self.max_quality)

    def update_sulfuras(self, item:Item) -> None:
        item.quality = 80

    def update_conjured(self, item:Item) -> None:
        item.sell_in -= 1
        item.quality -= 2
        item.quality = max(item.quality, self.min_quality) if item.quality < 0 else min(item.quality, self.max_quality)
