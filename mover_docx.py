import os
import shutil

def move_docx_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for file in os.listdir(source_dir):
        if file.endswith(".docx"):
            source_file = os.path.join(source_dir, file)
            destination_file = os.path.join(destination_dir, file)
            shutil.move(source_file, destination_file)
            print(f"Movido: {file} -> {destination_dir}")

if __name__ == "__main__":
    source_directory = "./documentacion_proyecto"
    destination_directory = "./ubicacion_remota"

    move_docx_files(source_directory, destination_directory)
    print("Fin.")
