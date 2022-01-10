import random
import uuid
from PIL import Image, ImageDraw


WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0,0,0)

def get_random_points(n_points, max_x, max_y):
    random_points = []
    for _ in range(n_points):
        point = (random.randint(0,max_x), random.randint(0,max_y))
        random_points.append(point)
    return random_points

def make_wall_drawing():
    run_id = uuid.uuid4()

    print(f'Processing run_id: {run_id}')

    image_widht = 4000
    image_height = 4000
    image = Image.new('RGB', size=(image_widht, image_height), color=WHITE_COLOR)
    draw_image = ImageDraw.Draw(image)

    random_points = get_random_points(50, image_widht, image_height)
    for point_1 in random_points:
        for point_2 in random_points:
            line = (point_1, point_2)
            line_color = (BLACK_COLOR)
            draw_image.line(line, fill=line_color)

    image.save(f'./output/Wall_drawing_{run_id}.png')


if __name__ == "__main__":
        make_wall_drawing()