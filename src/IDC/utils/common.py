import os 
import yaml 


def config(yaml_path):
    """
    Read yaml file and return a dictionary
    """
    with open(yaml_path, "r") as yaml_file:
        yaml_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return yaml_dict


