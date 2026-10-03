from Packages import circle, square, triangle
import logging
import os

LOG_DIR = "loggings"
LOG_FILE_NAME = "app.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    force=True
)

logging.info(f"circle_area: {circle.area(7)}")

logging.info(f"circle_circumference: {circle.circumference(7)}")

logging.info(f"square_area: {square.area(7)}")

logging.info(f"perimeter_square: {square.perimeter(7)}")

logging.info(f"area_triangle: {triangle.area(5, 10)}")

logging.info(f"perimeter_triangle: {triangle.perimeter(6, 8, 10)}")