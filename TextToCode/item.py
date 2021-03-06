class Item():
    def __init__(self, name):
        self._name = name
        self._description = None
        self._location = None
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    
