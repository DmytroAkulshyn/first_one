import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Input

DATASET_PATH = 'dataset/'

num_classes = len(os.listdir(DATASET_PATH))

class_mode = 'binary' if num_classes == 2 else "categorical"

train_datagen = ImageDataGenerator(
    rescale=1/255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)


train_data = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(128, 128),
    batch_size=32,
    class_mode=class_mode,
    subset="training"
)

val_data = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=(128, 128),
    batch_size=32,
    class_mode=class_mode,
    subset="validation"
)
model = Sequential([
    Input(shape=(128, 128, 3)),
    Conv2D(32, (3, 3), activation="relu"),
    MaxPool2D(2,2),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPool2D(2,2),
    Conv2D(128, (3, 3), activation="relu"),
    MaxPool2D(2,2),
    Flatten(),
    Dense(256, activation="relu"),
    Dense(1, activation="sigmoid") if class_mode == "binary"
        else Dense(num_classes, activation="softmax")
])

loss_function = "binary_crossentropy" if class_mode == "binary" else 'categorical_crossentropy'
model.compile(optimizer="adam", loss=loss_function, metrics=["accuracy"])
model.fit(train_data, validation_data=val_data, epochs=100)
test_loss, test_accuracy = model.evaluate(val_data)
print(f"Model accuracy according to validation: {test_accuracy:.2f}")

model.save('image_classifier.h5')