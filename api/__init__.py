import os
from distutils.util import strtobool
def get_list(var_name, default=None):
    value = os.getenv(var_name)

    return value.split(",") if value else default