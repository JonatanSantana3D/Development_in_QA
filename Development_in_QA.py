
import os
import shutil
import time
import argparse

def sync_folders(src, dest, log_file, interval):
    while True:
        for foldername, subfolders, filenames in os.walk(src):
            for filename in filenames:
                src_file = os.path.join(foldername, filename)
                dest_file = os.path.join(dest, filename)
                try:
                    shutil.copy2(src_file, dest_file)
                    with open(log_file, 'a') as f:
                        f.write(f'Copied file {src_file} to {dest_file}\n')
                    print(f'Copied file {src_file} to {dest_file}')
                except Exception as e:
                    with open(log_file, 'a') as f:
                        f.write(f'Failed to copy file {src_file} to {dest_file}: {str(e)}\n')
                    print(f'Failed to copy file {src_file} to {dest_file}: {str(e)}')
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sync two folders.')
    parser.add_argument('--src', required=True, help='Source folder')
    parser.add_argument('--dest', required=True, help='Destination folder')
    parser.add_argument('--log', required=True, help='Log file')
    parser.add_argument('--interval', type=int, default=60, help='Sync interval in seconds')
    args = parser.parse_args()
    sync_folders(args.src, args.dest, args.log, args.interval)