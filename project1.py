from pathlib import Path
#########################

def path_syn(u_in: str) -> str:
    """
    This function ensures that the inputed path follows
    the accepted criteria for a path in python.
    """
    u_list = list(u_in)
    for c in range(len(u_list)):
        if u_list[c] == "\\":
            u_list[c] = "/"

        else:
            pass
    u_in = "".join(u_list)
    return (u_in)


def user_path(u_in: str):
    """
    This function makes the input into a path data type.
    """
    p = Path(u_in)
    return p


def sorter(p_list: [Path]):
    """
    This function sorts the paths into the order we want it to be.
    """
    new_p_list = []
    main_temp_list = []
    for item in p_list:
        temp_list = []
        item = str(item)
        char_counter = item.count('\\')
        temp_list.append(item)
        temp_list.append(char_counter) #counts number of '\'
        main_temp_list.append(temp_list)
    main_temp_list.sort(key=lambda x:x[1]) #uses number of '\' as a key to sort

    for item in main_temp_list:
        new_p_list.append(item[0])

    return new_p_list
   
    


def d_funct(u_in: str):
    """
    This function displays only the files in the given path;
    it ignores the directories.
    """
    u_path = user_path(u_in)
    path_list = []
    for new in u_path.iterdir():
        if new.is_file() == True:
            path_list.append(new)
            
    return path_list


def r_funct(u_in: str, p_list: [Path]):
    """ 
    This function displays all the files in the given path,
    including the subdirectories.
    """
    u_path = user_path(u_in)
    
    for new in u_path.iterdir():
        if new.is_file() == True:
            p_list.append(new)
        else:
            r_funct(new, p_list)
            
    return p_list


def special_funct(p_list: [Path]):
    """
    This executes a new set of instructions upon the interested files.
    """
    #A - All files in our list are considered interesting.
    #N - Searches for files whose name exactly matches the name.
    #E - Searches for particular extensions (with or without '.').
    #T - Determines whether the text contains the given input.
    #< - Searches for files that are less than the given bytes.
    #> - Searches for files that are given than the given bytes.
    new_list = []
    while True:
        new_input = input()
        
        if new_input == "A":
            for item in p_list:
                new_list.append(item)
                print(item)
            return new_list
                
        elif new_input[0:2] == "N ":
            for item in p_list:
                temp = str(item)
                index = temp.rfind('\\')
                if new_input[2:] == str(temp[index+1: ]):
                    new_list.append(item)
                    print(item)
            return new_list
                    
        elif new_input[0:2] == "E ":
            if '.' in new_input:
                user_index = new_input.rfind('.')
                for item in p_list:
                    temp = str(item)
                    index = temp.rfind('.')
                    
                    if new_input[user_index+1:] == str(temp[index+1: ]):
                        new_list.append(item)
                        print(item)
                        
            else:
                for item in p_list:
                    temp = str(item)
                    index = temp.rfind('.')
                    if new_input[2:] == str(temp[index+1: ]):
                        new_list.append(item)
                        print(item)
                        
            return new_list

        elif new_input[0:2] == "T ":
            for item in p_list:
                try:
                    temp_file = open(item) 
                    temp_str = (temp_file.readlines())
            
                    for line in temp_str:
                        if line.find(new_input[2:]) != -1:
                            print(item)
                            new_list.append(item)
                            temp_file.close()
                            break
                except:
                    temp_file.close()
            return new_list

        elif new_input[0:2] == '< ':
            for item in p_list:
                if item.stat().st_size < int(new_input[2: ]):
                    new_list.append(item)
                    print(item)
            return new_list

        elif new_input[0:2] == '> ':
            for item in p_list:
                if item.stat().st_size > int(new_input[2: ]):
                    new_list.append(item)
                    print(item)
            return new_list
        
        else:
            """
            Determines whether the input is valid.
            """
            print("ERROR")
            pass

def mod_funct(m_list: [Path]):
    """
    This executes the final set of instructions upon the interested files.
    """
    #F - Prints first line of text from the given files.
    #D - Creates a duplicate file with the extension .dup.
    #T - Touches, modify the timestamp, all of the given files.
    while True:
        final_input = input()

        if final_input == 'F':
            for item in m_list:
                try:
                    temp_file = open(item) 
                    temp_str = (temp_file.readlines())
                    
                    for line in temp_str:
                        print(line[:-1])
                        break
        
                    temp_file.close()
                except:
                    print("NOT TEXT")
                    temp_file.close()
            break
        
        elif final_input == 'D':
            for item in m_list:
                new_item = str(item) + ".dup"
                
                infile = open(item)
                temp_str = infile.readlines()

                outfile = open(new_item, "w")
                for line in temp_str:
                    outfile.write(line)

                infile.close()
                outfile.close()
            break

        elif final_input == "T":
            for item in m_list:
                item = Path(item)
                item.touch()
            break
        
        else:
            """
            Determines whether the input is valid.
            """
            print("ERROR")
            pass

def main():
    """
    Calls and executes all the other functions.
    """
    while True:
        user_in = input()
        user_in = path_syn(user_in)
    
        if user_in[0:2] == 'D ':
            user_in = user_in[2:]
            
            path_list = d_funct(user_in)
            for item in path_list:
                print(item)
                
            mod_list = special_funct(path_list)
            mod_funct(mod_list)
            break
        elif user_in[0:2] == 'R ':
            user_in = user_in[2:]
            
            path_list = []
            path_list = r_funct(user_in, path_list)
            path_list = sorter(path_list)
            
            for item in path_list:
                print(item)
            
            mod_list = special_funct(path_list)
            mod_funct(mod_list)
            break

        else:
            """
            Determines whether the input is valid
            """
            print("ERROR")
            pass

main() 
 
