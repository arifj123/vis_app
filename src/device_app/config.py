# Change this directory when running on your computer!
#directory = "C:\\Users\\arifa\\Documents\\Vis-App-2\\device_app\\datasets\\"

import os, sys

current_directory = os.getcwd()

# Change this directory when running on your computer!
directory = current_directory + "\\src\\device_app\\datasets\\"


# Don't change anything below!
past_lst = ["Past Hour", "Past Day", "Past Week", "Past Month", "Past Year"]
# appliances_lst = ["dishwaser", "refrigerator", 
#                   "washer_dryer", "oven", 
#                   "kettle", "microwave", 
#                   "stove", "lighting", 
#                   "laptop", "tv"]
appliances_lst = ["dishwaser", "refrigerator", 
                  "washer_dryer"]
# images_lst = ["../assets/total_power.png", "../assets/dishwasher.png", 
#               "../assets/refrigerator.png", "../assets/washer_dryer.png",
#               "../assets/oven.png", "../assets/kettle.png", "../assets/microwave.png", 
#               "../assets/stove.png", "../assets/lighting.png", 
#               "../assets/laptop.png", "../assets/tv.png"]
images_lst = ["../assets/total_power.png", "../assets/dishwasher.png", 
              "../assets/refrigerator.png", "../assets/washer_dryer.png",]

print(directory)