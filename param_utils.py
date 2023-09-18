import sys
import re
from constants import POSSIBLE_TECHNIQUES

def param_checking(filename,percentage,technique):
    if len(sys.argv) != 4:
        print("You must provide exactly 3 parameters.")
        sys.exit(1)
    if not check_image_extension(filename):
        print("You must provide an image.")
        sys.exit(1)
    if percentage <= 0 or percentage >=100:
        print("You must provide a valid reduction percentage.")
        sys.exit(1)
    if technique not in POSSIBLE_TECHNIQUES:
        print("You must provide a valid reduction technique.")
        sys.exit(1)

def check_image_extension(filename):
    return bool(re.search(r'\.(png|jpg|jpeg|gif|bmp)$', filename, re.IGNORECASE))