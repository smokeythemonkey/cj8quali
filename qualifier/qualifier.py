from typing import Any, List, Optional
import itertools

"""Globals"""

vert = '\u2502'
hori = '\u2500'
left_cor_top = '\u250c'
mid_top = '\u252c'
right_cor_top = '\u2510'
mid_left = '\u251c'
center = '\u253c'
mid_right = '\u2524'
left_cor_bot = '\u2514'
mid_bot = '\u2534'
right_cor_bot = '\u2518'

newline = '\n'
blank = '\u0020'
padding = 2

def str_list(rows: List[List[Any]]):
    """
    function converts all elements of list into strings


    Args:
        rows (List[Any]): List of any type

    Returns:
        str_row (List[str]): return of list where all elements are string
    """    
    str_row = []
    
    if get_characteristic_list(rows) == True:
        for item in rows: 
            str_row.append([str(i) for i in item])           
    else:        
        str_row = [str(item) for item in rows]    
    
    
    return str_row

def get_table_settings(rows: List[List[Any]], labels: Optional[List[Any]] = None):
    """
    function creates dictionary of the width of each column based on rows w/ or w/o
    labels

    Args:
        rows (List): List of items to be displayed as table settings
        labels (List): List of labels for each columns

    Returns:
        tuple: tuple of each col length
    """    
    i = 0
    table_settings = []
    
    if labels != None:
        rows.append(labels)       
    row_transposed = list(map(list, itertools.zip_longest(*rows, fillvalue = blank)))
    if labels != None:
        rows.pop()
    for item in row_transposed:
        #width_col = get_width_column(item)
        table_settings.append(get_width_column(item))
        i += 1
    return tuple(table_settings)
    
def get_width_column(rows):    
    return len(max(rows, key = len)) + padding

def get_characteristic_list(rows: List[List[Any]]):
    return any(isinstance(x, List) for x in rows)

def get_len_list(rows: List[List[Any]]):
    return len(rows)



def build_row_string(item: str, centered: bool, width_col: int):
    if centered == False:
        item = item.ljust(width_col - padding)
        str_row = vert + blank + item + blank
    else:
        item = item.center(width_col, blank)
        if len(item) < (width_col):
            str_row = vert + item + blank 
        else:
            str_row = vert + item            

    
    return str_row

def build_top_border(table_settings):
    top = left_cor_top  
    for x, i in enumerate(table_settings):
        j=0
        while j != (i):
            top = top + hori
            j += 1
        if x == (len(table_settings)-1):
            top = top + right_cor_top
        else:
            top = top + mid_top
    
    return top + newline

def build_bot_border(table_settings):
    bot = left_cor_bot
    for x, i in enumerate(table_settings):    
            j=0
            while j != (i):
                bot = bot + hori
                j += 1
            if x == (len(table_settings)-1):
                bot = bot + right_cor_bot
            else:
                bot = bot + mid_bot
    return bot + newline

def build_heading_sep(table_settings):
    sep = mid_left
    for x, i in enumerate(table_settings):    
            j=0
            while j != (i):
                sep = sep + hori
                j += 1
            if x == (len(table_settings)-1):
                sep = sep + mid_right
            else:
                sep = sep + center
    return sep + newline



def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    rows = str_list(rows)  
    if labels != None:    
        labels = str_list(labels)   
    table_settings = get_table_settings(rows, labels)        
    # sum_items_rows = 

    
    
    str_table = build_top_border(table_settings) 
    if labels != None:
        for i, item in enumerate(labels):                   
            str_table = str_table + build_row_string(item, centered, table_settings[i])
            
            if i == (len(labels) - 1):               
                str_table = str_table + vert + newline
        # str_table = str_table 
        
        str_table = str_table + build_heading_sep(table_settings)   
    for item in rows:
        
        if len(rows) > 1:            
            for i, subitem in enumerate(item):                
                str_table = str_table + build_row_string(subitem, centered, table_settings[i]) 
                if i == (len(item) - 1):
                    str_table = str_table + vert
            str_table = str_table + newline
            
        else:
            for i, subitem in enumerate(item):
                str_table = str_table + build_row_string(subitem, centered, table_settings[i])                
            str_table = str_table + vert + newline
    
    str_table = str_table + build_bot_border(table_settings)
    
    return str_table
    

