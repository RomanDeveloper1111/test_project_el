from PIL import Image


def image_size(image_b, image_s):
    correct_format = ['jpeg', 'jpg', 'JPG', 'JPEG']
    with Image.open(image_b) as img_b:
        size_b_img = img_b.size
        with Image.open(image_s) as img_s:
            size_s_img = img_s.size
        if size_b_img[0] == 600 and size_b_img[1] == 1200 and img_b.format in correct_format:
            if size_s_img[0] == 300 and size_s_img[1] == 800 and img_s.format in correct_format:
                return {'img_b': 'correct', 'img_s': 'correct'}