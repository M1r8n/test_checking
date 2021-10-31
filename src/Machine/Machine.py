import enum


class States(enum.Enum):
    Busy = enum.auto()
    Free = enum.auto()
    Offline = enum.auto()


class Machine:
    state: States = States.Free

    def reserveMachine(self):
        if self.state == States.Free:
            self.state = States.Busy

    def checkState(self):
        return self.state

    def turnOff(self):
        self.state = States.Offline
