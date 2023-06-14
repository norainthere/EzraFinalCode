def evaluate_model(model, test_loader):
    # Evaluation loop
    with torch.no_grad():
        total_samples = 0
        total_correct = 0
        total_loss = 0.0

        for inputs, targets in test_loader:
            outputs = model(inputs)
            
            # Calculate loss
            loss = compute_loss(outputs, targets)
            total_loss += loss.item()

            # Calculate accuracy
            _, predicted = torch.max(outputs, dim=1)
            total_samples += targets.size(0)
            total_correct += (predicted == targets).sum().item()
        
        # Calculate average loss and accuracy
        average_loss = total_loss / len(test_loader)
        accuracy = total_correct / total_samples
        
        # Return the metrics
        return average_loss, accuracy
