import os
import subprocess
import shutil
from pathlib import Path


# =========================================================
# DESKTOP PATH
# =========================================================

def get_desktop_path():
    desktop = Path.home() / "Desktop"

    if desktop.exists():
        return desktop

    onedrive_desktop = Path.home() / "OneDrive" / "Desktop"

    if onedrive_desktop.exists():
        return onedrive_desktop

    # Fallback
    desktop.mkdir(parents=True, exist_ok=True)
    return desktop


# =========================================================
# OPEN FOLDER IN EXPLORER
# =========================================================

def open_explorer(folder_path):
    try:
        subprocess.Popen([
            "explorer.exe",
            str(folder_path)
        ])
        return True
    except Exception:
        return False


# =========================================================
# OPEN EXPLORER AND SELECT FILE
# =========================================================

def open_and_select_file(file_path):
    try:
        subprocess.Popen([
            "explorer.exe",
            "/select,",
            str(file_path)
        ])
        return True
    except Exception:
        return False


# =========================================================
# CREATE FILE
# =========================================================

def create_file(filename):

    desktop = get_desktop_path()

    filename = filename.strip()

    # Add .txt if no extension is provided
    if "." not in filename:
        filename += ".txt"

    file_path = desktop / filename

    try:

        file_path.touch(exist_ok=True)

        # Open Explorer and select the new file
        open_and_select_file(file_path)

        return f"{filename} created successfully on Desktop."

    except Exception as e:

        return f"Error creating file: {e}"


# =========================================================
# CREATE FOLDER
# =========================================================

def create_folder(folder_name):

    desktop = get_desktop_path()

    folder_name = folder_name.strip()

    folder_path = desktop / folder_name

    try:

        folder_path.mkdir(parents=True, exist_ok=True)

        # Open the newly created folder
        open_explorer(folder_path)

        return f"{folder_name} created successfully on Desktop."

    except Exception as e:

        return f"Error creating folder: {e}"


# =========================================================
# CREATE FILE INSIDE FOLDER
# =========================================================

def create_file_inside_folder(folder_name, filename):

    desktop = get_desktop_path()

    folder_name = folder_name.strip()
    filename = filename.strip()

    folder_path = desktop / folder_name

    try:

        # Create folder if it doesn't exist
        folder_path.mkdir(parents=True, exist_ok=True)

        # Add .txt if extension is missing
        if "." not in filename:
            filename += ".txt"

        file_path = folder_path / filename

        # Create file
        file_path.touch(exist_ok=True)

        # Open folder and select file
        open_and_select_file(file_path)

        return f"{filename} created inside {folder_name}."

    except Exception as e:

        return f"Error creating file inside folder: {e}"


# =========================================================
# RENAME FILE
# =========================================================

def rename_file(old_name, new_name):

    desktop = get_desktop_path()

    old_name = old_name.strip()
    new_name = new_name.strip()

    old_file = desktop / old_name
    new_file = desktop / new_name

    try:

        if not old_file.exists():
            return f"{old_name} not found."

        if new_file.exists():
            return f"{new_name} already exists."

        old_file.rename(new_file)

        # Show renamed file in Explorer
        open_and_select_file(new_file)

        return f"{old_name} renamed to {new_name}."

    except Exception as e:

        return f"Error renaming file: {e}"


# =========================================================
# DELETE FILE
# =========================================================

def delete_file(filename):

    desktop = get_desktop_path()

    filename = filename.strip()

    file_path = desktop / filename

    try:

        if not file_path.exists():
            return f"{filename} not found."

        if not file_path.is_file():
            return f"{filename} is not a file."

        file_path.unlink()

        # Show Desktop after deletion
        open_explorer(desktop)

        return f"{filename} deleted successfully."

    except Exception as e:

        return f"Error deleting file: {e}"


# =========================================================
# OPEN FILE
# =========================================================

def open_file(filename):

    desktop = get_desktop_path()

    filename = filename.strip()

    file_path = desktop / filename

    try:

        if not file_path.exists():
            return f"{filename} not found."

        if not file_path.is_file():
            return f"{filename} is not a file."

        # Open file with default Windows application
        os.startfile(str(file_path))

        return f"{filename} opened successfully."

    except Exception as e:

        return f"Error opening file: {e}"


# =========================================================
# LIST DESKTOP FILES
# =========================================================

def list_files():

    desktop = get_desktop_path()

    try:

        items = list(desktop.iterdir())

        if not items:
            return "Desktop is empty."

        result = "Desktop contents:\n"

        for item in items:

            if item.is_dir():
                result += f"📁 {item.name}\n"

            else:
                result += f"📄 {item.name}\n"

        return result

    except Exception as e:

        return f"Error listing Desktop files: {e}"


# =========================================================
# MOVE FILE
# =========================================================

def move_file(filename, folder_name):

    desktop = get_desktop_path()

    filename = filename.strip()
    folder_name = folder_name.strip()

    source = desktop / filename
    destination_folder = desktop / folder_name

    try:

        if not source.exists():
            return f"{filename} not found."

        if not source.is_file():
            return f"{filename} is not a file."

        if not destination_folder.exists():
            return f"{folder_name} folder not found."

        if not destination_folder.is_dir():
            return f"{folder_name} is not a folder."

        destination = destination_folder / filename

        if destination.exists():
            return f"{filename} already exists inside {folder_name}."

        shutil.move(str(source), str(destination))

        # Open destination folder and select moved file
        open_and_select_file(destination)

        return f"{filename} moved to {folder_name} successfully."

    except Exception as e:

        return f"Error moving file: {e}"


# =========================================================
# COPY FILE
# =========================================================

def copy_file(filename, folder_name):

    desktop = get_desktop_path()

    filename = filename.strip()
    folder_name = folder_name.strip()

    source = desktop / filename
    destination_folder = desktop / folder_name

    try:

        if not source.exists():
            return f"{filename} not found."

        if not source.is_file():
            return f"{filename} is not a file."

        if not destination_folder.exists():
            return f"{folder_name} folder not found."

        if not destination_folder.is_dir():
            return f"{folder_name} is not a folder."

        destination = destination_folder / filename

        if destination.exists():
            return f"{filename} already exists inside {folder_name}."

        shutil.copy2(
            str(source),
            str(destination)
        )

        # Open destination folder and select copied file
        open_and_select_file(destination)

        return f"{filename} copied to {folder_name} successfully."

    except Exception as e:

        return f"Error copying file: {e}"


# =========================================================
# OPEN FOLDER
# =========================================================

def open_folder(folder_name):

    desktop = get_desktop_path()

    folder_name = folder_name.strip()

    folder_path = desktop / folder_name

    try:

        if not folder_path.exists():
            return f"{folder_name} not found."

        if not folder_path.is_dir():
            return f"{folder_name} is not a folder."

        # Open folder
        open_explorer(folder_path)

        return f"{folder_name} folder opened successfully."

    except Exception as e:

        return f"Error opening folder: {e}"


# =========================================================
# DELETE FOLDER
# =========================================================

def delete_folder(folder_name, confirmed=False):

    desktop = get_desktop_path()

    folder_name = folder_name.strip()

    folder_path = desktop / folder_name

    try:

        if not folder_path.exists():
            return f"{folder_name} not found."

        if not folder_path.is_dir():
            return f"{folder_name} is not a folder."

        # Ask for confirmation
        if not confirmed:
            return f"CONFIRM_DELETE_FOLDER:{folder_name}"

        # Only delete empty folders
        if any(folder_path.iterdir()):
            return f"{folder_name} folder is not empty. Deletion cancelled."

        folder_path.rmdir()

        # Show Desktop after deletion
        open_explorer(desktop)

        return f"{folder_name} folder deleted successfully."

    except Exception as e:

        return f"Error deleting folder: {e}"


# =========================================================
# FIND / SEARCH FILE
# =========================================================

def find_file(search_name):

    desktop = get_desktop_path()

    search_name = search_name.strip()

    try:

        if not desktop.exists():
            return "Desktop folder not found."

        matches = []

        for file_path in desktop.rglob("*"):

            if file_path.is_file():

                if search_name.lower() in file_path.name.lower():

                    matches.append(file_path)

        if not matches:
            return f"No file found matching '{search_name}'."

        result = f"Found {len(matches)} file(s):\n"

        for match in matches:

            result += f"\n📄 {match}"

        return result

    except Exception as e:

        return f"Error searching files: {e}"