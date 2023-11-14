from PIL import Image


def image_processor(img_path, block_size, block_processor):
    img = Image.open(img_path)
    width, height = img.size

    cols = width // block_size
    rows = height // block_size
    for i in range(cols):
        for j in range(rows):
            left = i * block_size;
            top = j * block_size
            right = left + block_size;
            bottom = top + block_size
            block = img.crop((left, top, right, bottom))

            processed_block = block_processor(block)

            img.paste(processed_block, (left, top, right, bottom))

    img.show()


def block_processor(block):
    width, height = block.size

    sum = [0, 0, 0]
    for i in range(width):
        for j in range(height):
            pixel = block.getpixel((i, j))
            for k, _ in enumerate(sum):
                sum[k] += pixel[k]

    for i, _ in enumerate(sum):
        sum[i] //= width * height

    datas = [tuple(sum)] * width * height
    block.putdata(datas)

    return block


# 暂未考虑边界处理
if __name__ == "__main__":
    image_processor(r"C:\Users\16204\Pictures\Saved Pictures\nemo.jpg", 9, block_processor)
