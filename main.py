import random
import time

class FootstepPowerGeneration:
    def _init_(self, max_storage):
        self.max_storage = max_storage  # Maximum energy storage (Joules)
        self.current_energy = 0  # Initial energy storage (Joules)

    def generate_energy(self):
        # Simulate energy generated per footstep (between 0.03 and 0.08 Joules)
        energy = random.uniform(0.03, 0.08)
        self.current_energy += energy
        if self.current_energy > self.max_storage:
            self.current_energy = self.max_storage  # Cap energy to max storage
        print(f"Energy generated: {energy:.3f} Joules. Total energy: {self.current_energy:.3f} Joules")

    def use_energy(self, energy_needed):
        # Simulate using energy to power a device
        if self.current_energy >= energy_needed:
            self.current_energy -= energy_needed
            print(f"Used {energy_needed:.3f} Joules. Remaining energy: {self.current_energy:.3f} Joules.")
        else:
            print("Not enough energy to use. Generate more energy.")

    def check_status(self):
        # Check current energy status
        print(f"Current energy: {self.current_energy:.3f} Joules (Max: {self.max_storage} Joules)")

def main():
    system = FootstepPowerGeneration(max_storage=5.0)  # Set max energy storage to 5 Joules

    while True:
        print("\n1. Generate energy (footstep)")
        print("2. Use energy (power device)")
        print("3. Check energy status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            system.generate_energy()
        elif choice == '2':
            energy_needed = float(input("Enter energy needed (in Joules): "))
            system.use_energy(energy_needed)
        elif choice == '3':
            system.check_status()
        elif choice == '4':
            print("Exiting the simulation. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid number.")
        
        # Simulate time between footsteps
        time.sleep(1)

if _name_ == "_main_":
    main()
