import os

def remove_unlabeled_images(images_directory, labels_directory):
    
    labeled_files = {os.path.splitext(f)[0] for f in os.listdir(labels_directory) if f.endswith('.txt')}
    
    deleted_images_count = 0

    for image_filename in os.listdir(images_directory):
        if image_filename.endswith(('.jpg', '.jpeg', '.png')): 
            image_base_name = os.path.splitext(image_filename)[0]
            if image_base_name not in labeled_files:
                image_path = os.path.join(images_directory, image_filename)
                print(f"Removing unlabeled image: {image_path}")
                os.remove(image_path)  
                deleted_images_count += 1

    print(f"Total removed unlabeled images: {deleted_images_count}")

images_dir = 'images/'  
labels_dir = 'labels/'  
remove_unlabeled_images(images_dir, labels_dir)
