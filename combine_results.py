import os

def combine_text_files(folder_path, output_file):
    with open(output_file, 'w') as combined_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as current_file:
                    combined_file.write(current_file.read() + '\n')

# Specify the folder path where the text files are located
folder_path = input("Input folder name: ")

# Specify the name of the output combined text file
output_file = '.\\results\\combined_results_' + folder_path +  '.txt'

combine_text_files(".\\runs\\detect\\" + folder_path + "\\labels", output_file)

print(f'Combined text files from {folder_path} into {output_file}')

# Mapping of class numbers to class names
class_mapping = {
    0: "person", 1: "bicycle", 2: "car", 3: "motorcycle", 4: "airplane",
    5: "bus", 6: "train", 7: "truck", 8: "boat", 9: "traffic light",
    10: "fire hydrant", 11: "stop sign", 12: "parking meter", 13: "bench",
    14: "bird", 15: "cat", 16: "dog", 17: "horse", 18: "sheep", 19: "cow",
    20: "elephant", 21: "bear", 22: "zebra", 23: "giraffe", 24: "backpack",
    25: "umbrella", 26: "handbag", 27: "tie", 28: "suitcase", 29: "frisbee",
    30: "skis", 31: "snowboard", 32: "sports ball", 33: "kite",
    34: "baseball bat", 35: "baseball glove", 36: "skateboard", 37: "surfboard",
    38: "tennis racket", 39: "bottle", 40: "wine glass", 41: "cup",
    42: "fork", 43: "knife", 44: "spoon", 45: "bowl", 46: "banana",
    47: "apple", 48: "sandwich", 49: "orange", 50: "broccoli",
    51: "carrot", 52: "hot dog", 53: "pizza", 54: "donut", 55: "cake",
    56: "chair", 57: "couch", 58: "potted plant", 59: "bed",
    60: "dining table", 61: "toilet", 62: "tv", 63: "laptop",
    64: "mouse", 65: "remote", 66: "keyboard", 67: "cell phone",
    68: "microwave", 69: "oven", 70: "toaster", 71: "sink",
    72: "refrigerator", 73: "book", 74: "clock", 75: "vase",
    76: "scissors", 77: "teddy bear", 78: "hair drier", 79: "toothbrush"
}

# Initialize a dictionary to store the count of each class
class_count = {class_name: 0 for class_name in class_mapping.values()}

# Initialize a set to keep track of seen object IDs
seen_ids = set()

# Input file path (combined_results.txt) and output file path
input_file = '.\\results\\combined_results_' + folder_path +  '.txt'
output_file = '.\\results\\class_count.txt_' + folder_path +  '.txt'

# Process the input file line by line
with open(input_file, "r") as input_f:
    for line in input_f:
        parts = line.strip().split()
        if len(parts) >= 2:
            class_num = int(parts[0])
            if class_num in class_mapping:
                class_name = class_mapping[class_num]
                object_id = int(parts[-1])
                if object_id not in seen_ids:
                    class_count[class_name] += 1
                    seen_ids.add(object_id)

# Filter out classes with zero matches
class_count_filtered = {class_name: count for class_name, count in class_count.items() if count > 0}

# Write the results to the output file
with open(output_file, "w") as output_f:
    for class_name, count in class_count_filtered.items():
        output_f.write(f"{class_name}: {count}\n")

print("Class counts (excluding classes with zero matches) have been written to", output_file)

