import matplotlib.pyplot as plt
import numpy as np

def plot_raven_image(dataset_sample):
    example_set = dataset_sample["example_set"]
    candidates = dataset_sample["candidates"]

    # Create a figure with a 5x4 grid of images
    fig, axs = plt.subplots(5, 4, figsize=(16, 20))

    # Plot example images in top left 9 squares
    for i in range(example_set.shape[0]):
        row = i // 3
        col = i % 3
        axs[row, col].imshow(example_set[i, :, :])
        axs[row, col].set_title(f'Example {i}')

    # Plot candidate images in remaining squares
    for i in range(candidates.shape[0]):
        row = 3 + i // 4
        col = i % 4
        axs[row, col].imshow(candidates[i, :, :])
        axs[row, col].set_title(f'Candidate {i}')

    # Remove unused axes
    for i in range(3, 5):
        for j in range(4):
            if i * 4 + j >= example_set.shape[0] + candidates.shape[0]:
                axs[i, j].axis('off')

    plt.tight_layout()
    plt.show()

def plot_arc_data(datasample, idx=0):
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