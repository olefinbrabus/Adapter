
class OldSystem:
    def perform_old_operation(self):
        return "Old System Operation"

class NewSystem:
    def perform_new_operation(self):
        return "New System Operation"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def perform_new_operation(self):
        return f"Adapter: {self.old_system.perform_old_operation()}"

def client_code(system):
    return system.perform_new_operation()

old_system = OldSystem()

adapter = Adapter(old_system)

print("Client Code with New System:")
print(client_code(NewSystem()))

print("\nClient Code with Adapter:")
print(client_code(adapter))
