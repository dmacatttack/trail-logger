from pathlib import Path

# Folder containing the trail files
trail_folder = Path(r"D:\Users\danie\Project\Trail Logger\maps\trail")

# Folder where the trail log will be saved
log_folder = Path(r"D:\Users\danie\Project\Trail Logger\maps\logs")

# Create the logs folder if it doesn't already exist
log_folder.mkdir(parents=True, exist_ok=True)

# Find all JavaScript trail files
trail_files = sorted(trail_folder.glob("*.js"))

# Path for the log file
log_file = log_folder / "trails.txt"

# Write the trail filenames to the log
with open(log_file, "w", encoding="utf-8") as file:
    for trail in trail_files:
        file.write(trail.name + "\n")

print(f"Found {len(trail_files)} trail(s).")
print(f"Trail log created at:")
print(log_file)