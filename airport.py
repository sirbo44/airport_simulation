class Landing:
    def __init__(self, name: str, priority: int) -> None:
        self.name = name
        self.priority = priority
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return self.name + " priority: " + str(self.priority)

class LandingQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def landing_request(self, name: str, priority: int):
        node = Landing(name, priority)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            iter = self.head
            while iter is not None and iter.priority < priority:
                iter = iter.next
            if iter is None:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                if iter ==self.head:
                    iter.prev = node
                    node.next = iter
                    self.head = node
                else:
                    iter.prev.next = node
                    node.prev = iter.prev
                    iter.prev = node
                    node.next = iter
        if priority == 0:
            print("Flight", name, "requests landing")
        else:
            print("Flight", name, "requests emergency landing")
    
    def land(self):
        if self.tail is None: 
            return None
        elif self.tail == self.head:
            node = self.tail
            self.head = None
            self.tail = None
            
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        print("CONTROL:" , node.name, "land")
    
    def test(self):
        # visit and print each node, just for testing
        iter = self.head
        while iter is not None:
            print(iter)
            iter = iter.next



class Takeoff:
    def __init__(self, value: str) -> None:
        self.element = value
        self.next = None

    def __str__(self):
        return self.element
    
    def set_next(self, ref):
        self.next = ref

    def get_next(self):
        return self.next
    
    def get_element(self):
        return self.element


class TakeoffQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    def is_empty(self):
        return self.head is None and self.tail is None
    
    def takeoff_request(self, value):
        new_node = Takeoff(value)
        new_node.set_next(self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = self.head
        print("Flight", value, "requests takeoff")
        

    def takeoff(self):
        if not self.is_empty():
            if self.head == self.tail:
                value = self.tail.get_element()
                self.head = None 
                self.tail = None
            else:
                iterator = self.head
                while iterator.get_next() != self.tail:
                    iterator = iterator.get_next()
                value = self.tail.get_element()
                self.tail = iterator
                self.tail.set_next(None)
            print("CONTROL:", value, "takeoff")
        else:
            return None





if __name__ == "__main__":
    lq = LandingQueue()
    toq = TakeoffQueue()
    # # create the queues
    lq.landing_request("345", 0)
    lq.landing_request("190", 0)
    toq.takeoff_request("188")
    lq.land()
    lq.landing_request("621", 100)
    lq.land()
    toq.takeoff_request("511")
    lq.land()
    toq.takeoff()
    toq.takeoff()
    toq.takeoff_request("810")
    toq.takeoff()
    