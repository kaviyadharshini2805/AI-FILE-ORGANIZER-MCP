import os
import shutil

FOLDER_MAPPING = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".pdf": "PDFs",
    ".txt": "Documents",
    ".py": "Code"
}

def organize_folder(folder_path):

    print("Checking folder...")

    files = os.listdir(folder_path)

    print("Files found:", files)

    for file in files:

        file_path = os.path.join(folder_path, file)

        print("Processing:", file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1]

            print("Extension:", extension)

            if extension in FOLDER_MAPPING:

                target_folder = os.path.join(
                    folder_path,
                    FOLDER_MAPPING[extension]
                )

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(target_folder, file)
                )

                print(f"Moved {file} → {FOLDER_MAPPING[extension]}")

organize_folder("test_folder")