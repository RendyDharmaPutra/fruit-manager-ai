import csv
import os
import subprocess

def append_to_csv(row, path='datalatihreal.csv'):
    header = ['berat_buah', 'jarak', 'harga_bensin', 'cuaca', 'libur', 'persentase_cuaca', 'persentase_libur']
    file_exists = os.path.exists(path)

    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

def git_commit_and_push(file_path='datalatihreal.csv'):
    try:
        subprocess.run(['git', 'add', file_path], check=True)
        subprocess.run(['git', 'commit', '-m', 'Update datalatihreal.csv with new input data'], check=True)
        subprocess.run(['git', 'push'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Git Error: {e}")
