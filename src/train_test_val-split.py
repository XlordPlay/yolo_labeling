import os
import random
import shutil

def create_dataset_structure(base_dir):
    os.makedirs(os.path.join(base_dir, 'train/images'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'train/labels'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'val/images'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'val/labels'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'test/images'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'test/labels'), exist_ok=True)

def split_data(images_directory, labels_directory, base_dir, train_size=0.7, val_size=0.2):
    create_dataset_structure(base_dir)

    images = [f for f in os.listdir(images_directory) if f.endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    total_images = len(images)
    train_count = int(total_images * train_size)
    val_count = int(total_images * val_size)

    train_images = images[:train_count]
    val_images = images[train_count:train_count + val_count]
    test_images = images[train_count + val_count:]

    def copy_files(image_list, target_dir):
        for image in image_list:
            shutil.copy(os.path.join(images_directory, image), os.path.join(target_dir, 'images', image))
            label_file = os.path.splitext(image)[0] + '.txt'
            if os.path.exists(os.path.join(labels_directory, label_file)):
                shutil.copy(os.path.join(labels_directory, label_file), os.path.join(target_dir, 'labels', label_file))

    copy_files(train_images, os.path.join(base_dir, 'train'))
    copy_files(val_images, os.path.join(base_dir, 'val'))
    copy_files(test_images, os.path.join(base_dir, 'test'))

    print(f"Total images: {total_images}")
    print(f"Train images: {len(train_images)}")
    print(f"Validation images: {len(val_images)}")
    print(f"Test images: {len(test_images)}")

images_dir = 'images/'
labels_dir = 'labels/'
base_dir = 'dataset/'

split_data(images_dir, labels_dir, base_dir)
