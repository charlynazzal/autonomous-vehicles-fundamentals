# test_setup.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

print("🚗 Autonomous Vehicle Python Setup Test")
print("=" * 50)

# Test NumPy (for mathematical operations)
print("✅ NumPy version:", np.__version__)
vector = np.array([1, 2, 3])
print("   Vector test:", vector)

# Test Matplotlib (for visualization)
print("✅ Matplotlib version:", plt.matplotlib.__version__)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Setup Test - Sine Wave")
plt.show()

# Test Pandas (for data handling)
print("✅ Pandas version:", pd.__version__)
data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print("   DataFrame test:\n", data)

# Test OpenCV (for computer vision)
print("✅ OpenCV version:", cv2.__version__)
print("   OpenCV loaded successfully")

print("\n🎉 All libraries loaded successfully!")
print("Ready for autonomous vehicle programming!")