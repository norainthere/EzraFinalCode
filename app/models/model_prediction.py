def predict(model, inputs):
    with torch.no_grad():
        outputs = model(inputs)
    return outputs
