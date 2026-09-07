import subprocess


def open_application(app_name):
    app_name = app_name.lower().strip()

    applications = {
        "chrome": "chrome",
        "google chrome": "chrome",
        "notepad": "notepad",
        "calculator": "calc",
        "calc": "calc",
        "paint": "mspaint",
        "file explorer": "explorer",
        "explorer": "explorer",
    }

    if app_name not in applications:
        return f"I don't know how to open {app_name}."

    try:
        subprocess.Popen(
            applications[app_name],
            shell=True
        )

        return f"Opened {app_name} successfully."

    except Exception as e:
        return f"Could not open {app_name}: {e}"