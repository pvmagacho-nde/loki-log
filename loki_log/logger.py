"""
Version 0.1.0
"""
import inspect
import datetime
import os

# Constants for log levels
LOG_LEVEL_INFO = "INFO"
LOG_LEVEL_WARN = "WARN"
LOG_LEVEL_ERROR = "ERROR"
LOG_LEVEL_DEBUG = "DEBUG"

# Dynamically determine the base directory (the directory where this script resides or its parent)
BASE_DIR = os.getcwd()


def log_message(message: str, level: str = LOG_LEVEL_INFO, **kwargs):
    """
    Logs a structured message with optional contextual key-value pairs.

    Parameters:
    - message (str): The main log message.
    - level (str): The log level (INFO, WARN, ERROR, DEBUG). Defaults to INFO.
    - **kwargs: Optional key-value pairs to include in the log line.
    """
    frame = inspect.currentframe().f_back
    full_path = os.path.abspath(inspect.getfile(frame))

    # Use current working directory to get relative path for source
    try:
        relative_path = os.path.relpath(full_path, BASE_DIR)
    except ValueError:
        # If relpath fails (e.g., different drives on Windows), fallback to full path
        relative_path = full_path

    line_number = frame.f_lineno

    # Format timestamp
    now = datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z"

    # Format optional key=value pairs
    extras = " ".join(f"{k}={v}" for k, v in kwargs.items())
    extras_str = f" {extras}" if extras else ""

    # Final log output
    print(
        f'time={now} level={level} source={relative_path}:{line_number} msg="{message}"{extras_str}'
    )
