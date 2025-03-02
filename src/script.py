import imageio
import os

def split_videos_to_images(video_paths, output_folder, interval=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    saved_images = 0

    for video_path in video_paths:
        print(f"Processing video: {video_path}")
        reader = imageio.get_reader(video_path)
        
        for i, frame in enumerate(reader):
            if i % (reader.get_meta_data()['fps'] * interval) == 0:
                image_filename = os.path.join(output_folder, f'image_{saved_images + 1}.jpg')
                imageio.imwrite(image_filename, frame)
                saved_images += 1

    print(f"Saved {saved_images} images to {output_folder}")

# Пример использования
video_files = [
    "video/видео_1.mp4",
    "video/видео_2.mp4",
    "video/видео_3.mp4",
    "video/видео_4.mp4",
    "video/видео_5.mp4",
    "video/видео_6.mp4"
]

output_directory = 'images'
split_videos_to_images(video_files, output_directory, interval=10)
