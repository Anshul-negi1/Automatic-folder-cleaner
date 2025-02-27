import os

def create_folder(folder):
    os.makedirs(folder, exist_ok=True)

def move_files(folder, files):
    for file in files:
        os.replace(file, os.path.join(folder, file))

if __name__ == "__main__":
    files = [f for f in os.listdir() if os.path.isfile(f) and f != "main.py"]

    categories = {
        "Images": [".png", ".jpg", ".jpeg"],
        "Docs": [".txt", ".docx", ".doc", ".pdf"],
        "Media": [".mp4", ".mp3", ".flv"],
    }

    organized_files = {key: [] for key in categories}
    others = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        for category, extensions in categories.items():
            if ext in extensions:
                organized_files[category].append(file)
                break
        else:
            others.append(file)

    for category, files in organized_files.items():
        create_folder(category)
        move_files(category, files)

    if others:
        create_folder("Others")
        move_files("Others", others)

    print("Files have been organized successfully!")