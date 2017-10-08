from pathlib import Path
#########################
def read()-> str:
    '''Accepts the input'''
    
    user_input = input() 
    return user_input

def interpret(n:str)-> list:
    '''Interprets the input'''

    work_type = str(n[:2])
    path_way = Path(n[2:].replace( '\\' , '/'))
    return [work_type, path_way]

def d(n: Path)-> list:
    d_list = []
    for x in n.iterdir():
        if x.is_file() == True:
            d_list.append(x)
    return d_list
            
    
def main():
   
    p=interpret(read())
    
    if p[0] == 'D ':
        a = sorted(d(p[1]))
        for b in a:
            print(b)
    elif p[0] == 'R ':
        r(p[1])
    else:
        print('Error')

def sort_v(n: list) -> list:
    a = sorted(n)
    return a

x = ['alex', 'hello', 'boo', 'alexander', 'booboo', 'bio']

#print(sort_v(d))
main()
#bloop bloop
