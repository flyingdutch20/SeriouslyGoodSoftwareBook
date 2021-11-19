# build a Container class, endowed with a public constructor that takes no arguments
# and creates an empty container
# A connection between two containers is symmetric: water can flow in both directions.
# A set of containers connected by symmetric links form what is known in computer
# science as an undirected graph.

class Container:
    def __init__(self):
        self.group = null
        self.connections = []
    def get_amount(self):
        return self.group.water_per_container()
    def connect_to(self, container):
        container.reverse_connect(self)
        self.connections.append(container)
        self.group.add_container(container)
    def reverse_connect(self, container):
        self.connections.append(container)
    def add_water(self, amount):
        self.group.add_water(amount)

class ContainerGroup:
    def __init__(self):
        self.containers = []
        total_water = 0
    def add_container(self, container):
        if not self.containers.includes(container):
            containers.append_all(container.group)
            self.add_water(container.group.total_water)
    def add_water(self, amount):
        total_water += amount
    def water_per_container(self):
        return (self.total_water / self.containers.size())


# public double getAmount()—Return the amount of water currently held in
# this container

# public void connectTo(Container other)—Permanently connect this container with other

# public void addWater(double amount)—Pour amount units of water into this
# container. This method automatically and equally distributes water among all
# containers that are connected, directly or indirectly, to this one.
# You can also use this method with a negative amount to remove water from
# this container. In that case, the group of connected containers should be
# holding enough water to satisfy the request—you wouldn’t want to leave a negative
# amount of water in a container.
