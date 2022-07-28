import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential() #Basic neural network structure
model.add(tf.keras.layers.Flatten(input_shape=(28, 28))) #Input layer
model.add(tf.keras.layers.Dense(512, activation='relu')) #First hidden layer
model.add(tf.keras.layers.Dense(512, activation='relu')) #Second hidden layer
model.add(tf.keras.layers.Dense(10, activation='softmax')) #Output layer

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=50) #Train model
model.save('handwritten4.model')