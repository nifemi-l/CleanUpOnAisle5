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
        if item.is_file() and item not in ('desktop.ini', '.DS_Store'):
            # delete the file 
            item.unlink()
            print(f"{item} was successfully deleted.\n")
    
    # end time
    end_time = time.time()

    # get elapsed time
    elapsed_time = round(end_time - start_time, 4)

    print(f"Process completed in {elapsed_time} seconds.")

def main(): 
    while True: 
        try:
            dir_input = input("Enter path to directory\n(Enter 'e' to exit)\n: ").strip()
            if not dir_input:
                raise TypeError
            if dir_input.lower() == 'e':
                print('Goodbye!')
                break
            clear_dir(dir_input)
            break
        except TypeError: 
            print("\nPath cannot be empty.\n")
        except Exception as e:
            print(f'\n{e}\n') 
main()