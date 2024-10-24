import os
import argparse

def add_to_path(directory):
    """Add specified directory to system PATH environment variable."""
    # Convert to absolute path and normalize
    directory = os.path.abspath(os.path.normpath(directory))
    
    current_path = os.environ['PATH']
    if directory not in current_path:
        new_path = current_path + ';' + directory
        os.environ['PATH'] = new_path
        return f"{directory} added to PATH successfully."
    return f"{directory} is already in PATH."

def main():
    parser = argparse.ArgumentParser(description='Add a directory to system PATH')
    parser.add_argument('directory', help='Directory path to add to PATH')
    parser.add_argument('--check', action='store_true', help='Check if directory is already in PATH')
    
    args = parser.parse_args()
    
    if args.check:
        if args.directory in os.environ['PATH']:
            print(f"{args.directory} is in PATH")
        else:
            print(f"{args.directory} is not in PATH")
    else:
        result = add_to_path(args.directory)
        print(result)

if __name__ == "__main__":
    main()
