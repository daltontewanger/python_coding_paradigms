'''
Functional prompt
'''
def flat_sort(array):
    new_array = []
    for item in array:
        try:
            # first try to iterate over an item if present first
            for i in item:
                new_array.append(i)
        except:
            # if it is not an item then just append it
            new_array.append(item)
    # now sort the array
    return sorted(new_array)

# test an array that can be flattened
print(flat_sort([10, [3, 5], 7, [2, 8, 6], [1, 9, 4]]))

'''
Object Oriented Prompt
'''
# Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
'''
Define a new class, AnakinsPod that inherits the Podracer class,
but also contains a special method called boost that will multiply max_speed by 2.
'''
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2
        
'''
Define another class that inherits Podracer and call this one SebulbasPod. 
This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self):
        self.condition = "trashed"

# create Obi-Wan's pod, check its condition, run the repair method, and check it again
obi_wan_pod = Podracer(400, "perfect", 150000)
print(obi_wan_pod.condition)
obi_wan_pod.repair()
print(obi_wan_pod.condition)

# create Anakin's pod, check its speed, run the boost method, and check it again
anakin_pod = AnakinsPod(500, "perfect", 90000)
print(anakin_pod.max_speed)
anakin_pod.boost()
print(anakin_pod.max_speed)

# create Sebulba's pod, check its condition, run the flame_jet method, and check it again
sebulba_pod = SebulbasPod(600, "perfect", 200000)
print(sebulba_pod.condition)
sebulba_pod.flame_jet()
print(sebulba_pod.condition)