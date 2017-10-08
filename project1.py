from pathlib import Path

def path_syn(u_in: str) -> str:
    u_list = list(u_in)
    for c in range(len(u_list)):
        if u_list[c] == "\\":
            u_list[c] = "/"
            
        else:
            pass
    u_in = "".join(u_list)
    return (u_in)


def user_path(u_in):
    p = Path(u_in)
    return p


def d_funct(u_in: str):
    u_path = user_path(u_in)
    path_list = []
    for new in u_path.iterdir():
        if new.is_file() == True:
            path_list.append(new)
            
    return path_list


def r_funct(u_in: str, p_list):
    u_path = user_path(u_in)
    
    for new in u_path.iterdir():
        if new.is_file() == True:
            p_list.append(new)
        else:
            r_funct(new, p_list)
            
    return p_list


def special_funct(p_list):
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
            print("ERROR")
            pass

def mod_funct(m_list):
    while True:
        final_input = input()

        if final_input == 'F':
            for item in m_list:
                try:
                    temp_file = open(item) 
                    temp_str = (temp_file.readlines())

                    for line in temp_str:
                        print(line)
                        temp_file.close()
                        break
                except:
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
                item.touch()
            break
        
        else:
            print("ERROR")
            pass

def main():
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
            for item in path_list:
                print(item)
            
            mod_list = special_funct(path_list)
            mod_funct(mod_list)
            break
        else:
            print("ERROR")
            pass

main() 
