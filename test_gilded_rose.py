from gilded_rose import Item, GildedRose

#Function tests
def test_normal_item_quality_and_sell_in_degrade_by_one():
    items = [Item("+5 Dexterity Vest", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 19

#Once the sell by date has passed, Quality degrades twice as fast
def test_normal_item_quality_degrades_twice_as_fast_after_sell_in_date():
    items = [Item("+5 Dexterity Vest", -1, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -2
    assert items[0].quality == 18

#The Quality of an item is never negative
def test_normal_item_quality_is_never_negative():
    items = [Item("+5 Dexterity Vest", 10, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 0

def test_normal_item_quality_is_never_negitive_even_when_passed():
    items = [Item("+5 Dexterity Vest", 10, -1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 0

#The Quality of an item is never more than 50
def test_normal_item_quality_cant_be_more_than_50():
    items = [Item("+5 Dexterity Vest", 10, 51)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 50

#The Quality of an item is never more than 50
def test_normal_item_quality_cant_be_more_than_50_even_when_passed():
    items = [Item("+5 Dexterity Vest", 10, 55)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 50

def test_aged_brie_increases_quality_with_age():
    items = [Item("Aged Brie", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 21
    
def test_aged_brie_quality_increases_twice_as_fast_after_sell_in_date():
    items = [Item("Aged Brie", -1, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -2
    assert items[0].quality == 22

#"Sulfuras", being a legendary item, never has to be sold or decreases in Quality    
def test_sulfuras_legendary_item_never_changes_sell_in_quality():
    items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80

#Just for clarification, an item can never have its Quality increase above 50, 
# however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
def test_sulfuras_quality_is_80():
    items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80
    
def test_backstage_passes_increase_in_quality_as_sell_in_date_approaches():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 14
    assert items[0].quality == 21

def test_backstage_passes_increase_in_quality_by_2_when_sell_in_date_is_10_or_lower():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 22

def test_conjured_item_degrades_twice_as_fast_as_normal_item():
    items = [Item("Conjured", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 18






