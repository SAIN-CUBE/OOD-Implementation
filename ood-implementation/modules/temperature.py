
class TemperatureController:
    def __init__(self, room, current_temp):
        self.room = room
        self.current_temp = current_temp

    def adjust_temperature(self, target_temp):
        print(f"Adjusting temperature in {self.room} from {self.current_temp}°C to {target_temp}°C.")
        self.current_temp = target_temp
