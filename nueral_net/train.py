# simple function to train the RNN

def train(model, train_generator):
    num_epochs = 25
    model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

    return model

    