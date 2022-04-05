from items import Item, ItemWithName
if __name__ == '__main__':
    item1 = Item(1, 2)
    item2 = ItemWithName('gold', 1, 2)

    print(item1)
    print(item2)
    a= [item1, item2]
    print(a)
