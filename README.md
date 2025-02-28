File Organizer Script  

A simple Python script to automatically organize files in a directory by categorizing them into folders based on their file types.  

 Features  

- Creates necessary folders if they don’t exist.  
- Moves files into appropriate folders based on their extensions.  
- Helps keep directories clean and organized.  

 Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/Anshul-negi1/file-organizer.git
   cd file-organizer

   Usage

Run the script in the directory where you want to organize files:
python main.py

This will create the following folders and move files accordingly:
	•	Images: .png, .jpg, .jpeg
	•	Docs: .txt, .docx, .doc, .pdf
	•	Media: .mp4, .mp3, .flv
	•	Others: Any other file types

Example

Before Running the Script:

/Downloads
  ├── image1.jpg
  ├── document.docx
  ├── song.mp3
  ├── video.mp4
  ├── random.exe

After Running the Script:

/Downloads
  ├── Images
  │    ├── image1.jpg
  │  
  ├── Docs
  │    ├── document.docx
  │  
  ├── Media
  │    ├── song.mp3
  │    ├── video.mp4
  │  
  ├── Others
  │    ├── random.exe
   
