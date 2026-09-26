files = [
    {"name": "lecture.mp4", "type": "video", "size_mb": 850.5},
    {"name": "notes.pdf", "type": "document", "size_mb": 12.4},
    {"name": "game.zip", "type": "archive", "size_mb": 2400.0},
    {"name": "project.py", "type": "code", "size_mb": 0.8},
    {"name": "vacation.mp4", "type": "video", "size_mb": 1250.7},
    {"name": "resume.pdf", "type": "document", "size_mb": 2.1},
]




def total_size(files):
    total = sum (file['size_mb'] for file in files)
    return total

def average_size(files):
    total = total_size(files)
    avg = total/ len(files)
    return avg

def largest_file(files):
    largest = files[0]
    for file in files[1:]:
        if file['size_mb'] > largest['size_mb']:
            largest = file
            
    return largest 

def large_file(files, limit):
    large_files = []

    for file in files:
        if file["size_mb"] > limit:
            large_files.append(file)

    return large_files
            
    

if __name__ == "__main__":
        print(f"Total size: {total_size(files):.2f}")
        print(f"Average size: {average_size(files):.2f}")
        largest = largest_file(files)
        print(f"Largest file: {largest['name']} - {largest['size_mb']}")
        
        limit = 1000
        large_files = large_file(files, limit)
        print(f"Files over {limit} MB:")

        for file in large_files:
             print(f"{file['name']} - {file['size_mb']:.2f} MB")
