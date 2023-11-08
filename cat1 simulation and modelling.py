import math

class Gun:
    def __init__(self, bullet_mass, bullet_velocity):
        self.bullet_mass = bullet_mass  # Mass of the bullet in kg
        self.bullet_velocity = bullet_velocity  # Velocity of the bullet in m/s

class Bullet:
    def __init__(self, gun):
        self.mass = gun.bullet_mass
        self.velocity = gun.bullet_velocity
        self.distance_travelled = 0
        self.fired = False

    def fire(self):
        self.fired = True

    def update_position(self, time):
        if self.fired:
            self.distance_travelled += self.velocity * time

def main():
    # Create a gun with specified parameters
    star_handgun = Gun(bullet_mass=0.01, bullet_velocity=400)  # Example values

    # Create a bullet
    bullet = Bullet(star_handgun)

    # Fire the bullet
    bullet.fire()

    # Simulate the bullet's motion
    time_step = 0.01  # Time step in seconds
    while bullet.distance_travelled < math.pi:
        bullet.update_position(time_step)

    # Check if the bullet impacts
    if bullet.distance_travelled >= math.pi:
        print("The bullet has impacted.")

if __name__ == "__main__":
    main()
