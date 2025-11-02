# I'm renaming the dataset for consistency so later scripts always reference the same filename.

import argparse
from pathlib import Path
import zipfile
import shutil

# Function to unzip if necessary
def maybe_unzip(input_path: Path, extract_dir: Path) -> Path:
    if input_path.suffix.lower() == '.zip':
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(input_path, 'r') as z:
            z.extractall(extract_dir)
        csvs = list(extract_dir.rglob('*.csv'))
        if not csvs:
            raise FileNotFoundError('No CSV file found inside the zip archive.')
        return csvs[0]
    return input_path

# Copy the file to the target name
def rename_to_target(src_csv: Path, out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_csv, out_csv)

# Main CLI entry point
def main():
    parser = argparse.ArgumentParser(description='Prepare Netflix dataset')
    parser.add_argument('--in', dest='inp', required=True, help='Input dataset path (e.g., data/netflix_data.csv)')
    parser.add_argument('--out', dest='outp', required=True, help='Output renamed path (e.g., data/Netflix_shows_movies.csv)')
    args = parser.parse_args()

    inp = Path(args.inp)
    outp = Path(args.outp)
    source_csv = maybe_unzip(inp, extract_dir=outp.parent / '.extracted')
    rename_to_target(source_csv, outp)
    print(f'Successfully prepared file → {outp}')

if __name__ == '__main__':
    main()