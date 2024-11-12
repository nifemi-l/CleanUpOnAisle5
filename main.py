import pathlib
import time

def clear_dir(directory): 
    """Clear the contents of a directory."""
    # start time
    start_time = time.time()

    dir_path = pathlib.Path(directory)

    # sanitize
    if not dir_path.is_dir(): 
        raise ValueError(f"{dir_path} is not a valid directory.")
    
    print("\n**WET FLOOR -- CAUTION**")
    for item in dir_path.iterdir(): 
        if item.is_file() and item != 'desktop.ini':
            # delete the file 
            item.unlink()
            print(f"{item} was successfully deleted.\n")
    
    # end time
    end_time = time.time()

    # get elapsed time
    elapsed_time = round(end_time - start_time, 2)

    print(f"Process completed in {elapsed_time} seconds.")

def main(): 
    dir_input = input('Enter path to directory: ')    
    clear_dir(dir_input)

main()