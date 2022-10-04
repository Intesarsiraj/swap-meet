class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor = None):
        first_item = self.inventory[0]
        first_item_vendor = other_vendor.inventory[0]
        # vendor_empty_list = []
        # self_empty_list = []
        if first_item in self.inventory and first_item_vendor in other_vendor.inventory:
            self.remove(first_item)
            other_vendor.add(first_item)
            self.add(first_item_vendor)
            other_vendor.remove(first_item_vendor)
            return True
        elif self.inventory and other_vendor == None:
            return False
        
    
    
    




        
