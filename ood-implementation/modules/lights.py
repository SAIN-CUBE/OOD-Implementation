
class LightsController:
    def __init__(self, room):
        self.room = room
        self.status = "off"

    def toggle_lights(self):
        if self.status == "off":
            print(f"Turning on the lights in the {self.room}.")
            self.status = "on"
        else:
            print(f"Turning off the lights in the {self.room}.")
            self.status = "off"
