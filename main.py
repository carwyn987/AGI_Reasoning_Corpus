from src.readers import *


if __name__ == "__main__":

    raven_obj = RAVEN_Reader()
    raven_obj.get_all_sub_data_dirs(intermediate_dir='')
    
    # Walk the folder files
    for root, dirs, files in os.walk(raven_obj.sub_data_dirs[0]):
        for file in files:
            if file.endswith('.npz'):
                # Read the npz file
                npz_file = read_npz_file(os.path.join(root, file))
                # Extract the npz data
                npz_data = extract_npz_data(npz_file)
                # Get the image data
                image = npz_data['image']
                # Plot the image
                plot_npz_image(image)