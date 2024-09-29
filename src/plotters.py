import matplotlib.pyplot as plt
import numpy as np

def plot_npz_image(image):
    # Plot first 8 images in a 3x3 matrix
    fig, axs = plt.subplots(3, 3, figsize=(12, 12))
    for i in range(8):
        axs[i // 3, i % 3].imshow(image[i, :, :])
        axs[i // 3, i % 3].set_title(f'Channel {i}')
    # Remove unused subplot
    axs[2, 2].axis('off')
    plt.tight_layout()

    # Plot the rest 8 images in a 2x4 matrix
    fig, axs = plt.subplots(2, 4, figsize=(16, 8))
    for i in range(8):
        axs[i // 4, i % 4].imshow(image[i+8, :, :])
        axs[i // 4, i % 4].set_title(f'Channel {i+8}')
    plt.tight_layout()
    plt.show()

def plot_arc_data(datasample):
    # Get the train and test data
    train_data = datasample['train']
    test_data = datasample['test'][0]

    # Create a figure with n rows and 4 columns
    n = len(train_data)
    fig, axs = plt.subplots(n, 4, figsize=(20, n*2))

    # Plot the train data
    for i, train_example in enumerate(train_data):
        train_input = np.array(train_example['input'])
        train_output = np.array(train_example['output'])
        
        axs[i, 0].imshow(train_input, cmap='viridis')
        axs[i, 0].set_title('Train Input')
        axs[i, 0].axis('off')

        axs[i, 1].imshow(train_output, cmap='viridis')
        axs[i, 1].set_title('Train Output')
        axs[i, 1].axis('off')

    # Plot the test data
    test_input = np.array(test_data['input'])
    test_output = np.array(test_data['output'])

    for i in range(n):
        axs[i, 2].imshow(test_input, cmap='viridis')
        axs[i, 2].set_title('Test Input')
        axs[i, 2].axis('off')

        axs[i, 3].imshow(test_output, cmap='viridis')
        axs[i, 3].set_title('Test Output')
        axs[i, 3].axis('off')

    plt.tight_layout()
    plt.show()