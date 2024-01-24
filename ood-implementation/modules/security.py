
class SecuritySystem:
    def __init__(self):
        self.armed = False

    def arm(self):
        print("Arming the security system.")
        self.armed = True

    def disarm(self):
        print("Disarming the security system.")
        self.armed = False
