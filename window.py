import arcade
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "My Game"

# 0-10 scale for each need
CITIZEN_NEEDS = {
    "Renewable Energy": 2,
    "Clean Water": 7
}

class Citizen:
    def __init__(self):
        self.needs = CITIZEN_NEEDS.copy()
        self.baseline_happiness = 50
        self.happiness = self.baseline_happiness
    
    def update_happiness(self, satisfaction_scores):
        weighted_sum = sum(self.needs[idx] * satisfaction_scores[idx] for idx in self.needs)
        total_importance = sum(self.needs.values())
        self.happiness = self.baseline_happiness + (weighted_sum / total_importance)

class City:
    def __init__(self):
        self.needs = CITIZEN_NEEDS.keys()
        self.satisfaction_scores = {need: 0 for need in self.needs}
    
    def compute_satisfaction(self):
        for need in self.needs:
            self.satisfaction_scores[need] = random.randint(-100, 100)

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.total_time = 0.0

    def setup(self):
        self.city = City()
        self.citizen = Citizen()

        print(f"Citizen Happiness = {self.citizen.happiness}")
    
    def on_update(self, dt):
        self.total_time += dt

        if self.total_time >= 5.0:
            self.total_time = 0.0

            self.city.compute_satisfaction()
            self.update_citizen_happiness()
            
            print(f"Citizen Happiness = {self.citizen.happiness}")

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here

    def update_citizen_happiness(self):
        self.citizen.update_happiness(self.city.satisfaction_scores)

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()