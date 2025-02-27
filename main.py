import os

def create_and_move_files(folder, files):
    if files:
        os.makedirs(folder, exist_ok=True)
        for file in files:
            os.replace(file, os.path.join(folder, file))

def organize_files():
    files = [f for f in os.listdir() if os.path.isfile(f) and f != "main.py"]
    
    categories = {
        "Images": {".png", ".jpg", ".jpeg"},
        "Docs": {".txt", ".docx", ".doc", ".pdf"},
        "Media": {".mp4", ".mp3", ".flv"}
    }
    
    organized_files = {category: [] for category in categories}
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
        create_and_move_files(category, files)
    
    create_and_move_files("Others", others)
    
    print("Files have been organized successfully!")

if __name__ == "__main__":
    organize_files()