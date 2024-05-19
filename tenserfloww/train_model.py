import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load data
chestXray = np.load("chestXray.npy")
labels = np.load("labels.npy")

# Shuffle data
s = np.arange(chestXray.shape[0])
np.random.shuffle(s)
chestXray = chestXray[s]
labels = labels[s]

# Split data
train_size = int(0.9 * len(chestXray))
x_train, x_test = chestXray[:train_size], chestXray[train_size:]
y_train, y_test = labels[:train_size], labels[train_size:]

# Normalize data
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Build model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(180, 180, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(6, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
history = model.fit(x_train, y_train, epochs=50, validation_data=(x_test, y_test))

# Save model
model.save("model.h5")

# Plot training history
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

