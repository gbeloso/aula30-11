from src.entities.errors.duplicateitemerror import DuplicateItemError


class TodoList:
    def __init__(self, owner):
        self.owner = owner
        self.list = []

    def add(self, item):
        self.check_duplicate(item.description)
        self.list.append(item)
        self.sort()

    def get(self, index):
        return self.list[index]

    def get_owner(self):
        return self.owner

    def complete(self, index):
        self.list[index].complete()
        self.sort()

    def remove(self, index):
        self.list.pop(index)

    def size(self):
        return len(self.list)

    def find(self, description):
        for item in self.list:
            if item.description == description:
                return item

    def sort(self):
        self.list.sort()

    def change_priority(self, index, new_priority):
        self.list[index].change_priority(new_priority)
        self.list.sort()

    def change_description(self, old_desc, new_desc):
        item = self.find(old_desc)
        self.check_duplicate(new_desc)
        if item:
            item.description = new_desc
        
    def check_duplicate(self, desc):
        dup_item = self.find(desc)
        if dup_item != None:
            raise DuplicateItemError()

    def complete_item_by_desc(self, desc):
        item = self.find(desc)
        if item != None:
            item.complete()
        self.sort()