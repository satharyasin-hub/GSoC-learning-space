from model import SchellingModel

model = SchellingModel()

for i in range(20):
    model.step()
    print(f"Step {i} completed")