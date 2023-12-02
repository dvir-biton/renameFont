import os
import sys

def rename_fonts(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".ttf"):
            new_name = filename.lower().replace("-", "_")
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

if __name__ == "__main__":
    folder_arg = sys.argv[1] if len(sys.argv) > 1 else "."

    try:
        rename_fonts(folder_arg)
        print("Fonts successfully renamed!")
    except Exception as e:
        print(f"An error occurred: {e}")
