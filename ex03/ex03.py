from datetime import datetime
from pathlib import Path


def smart_log(*args, **kwargs)->None:
    message = " ".join(str(a) for a in args)

    if kwargs.get("timestamp", False):
        now = datetime.now()
        message = f"{now.strftime('%Y-%m-%d %H:%M')} {message}"

    match kwargs.get("level", "log"):
        case "info":
            color, tag = "\033[94m", "INFO"
        case "warning":
            color, tag = "\033[93m", "WARNING"
        case "error":
            color, tag = "\033[91m", "ERROR"
        case "debug":
            color, tag = "\033[90m", "DEBUG"
        case _:
            color, tag = "\033[97m", "log"

    if kwargs.get("save_to", False):
        file = "app.log"
        Path(file).parent.mkdir(parents=True, exist_ok=True)

        with open(file, "a", encoding="utf-8") as f:
            f.write(f"[{tag}] " + message + "\n")

    if kwargs.get("color") is False:
        color = "\033[97m"

    print(f"{color}[{tag}] {message}\033[0m")


if __name__ == "__main__":
    smart_log("System started successfully",level="info")
    smart_log("uninitialised var",level="warning", timestamp=True)
    smart_log(level="debug", timestamp=True, color=False)
    smart_log("testtest")
    smart_log(level="error", timestamp=True, save_to=True)
    smart_log("test warning", level="debug", timestamp=True, save_to=True)