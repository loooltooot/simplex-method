import copy

class matrix_():
    
    """
        Class that represents a matrix with fields:
            .rows
            .columns
            .matrix
            
        You should use .__str__() instead of str() to
        get correct matrix representation
    """
    
    def __init__(self, rows=3, columns=3):
        self.rows, self.columns = rows, columns
        self.matrix = [[0 for x in range(columns)] for x in range(rows)]
    
    
    def __str__(self, margin=0):
        max_lengths_list = [0 for x in range(self.columns)]
        for i in range(self.columns):
            for j in range(self.rows):
                if len(str(self.matrix[j][i])) > max_lengths_list[i]:
                    max_lengths_list[i] = len(str(self.matrix[j][i]))
                    
        for i in range(self.rows):
            if i > 0:
                print(" " * margin, end="")
            for j in range(self.columns):
                item = str(self.matrix[i][j])
                while len(item) < max_lengths_list[j]:
                    if len(item) <= max_lengths_list[j] - 2: 
                        item += " "
                    item = item.rjust(len(item) + 1)
                print(f"| {item} ", end="")
            
            print("|")

def simplex_method(table: matrix_, order: list=[]):
    new_table = copy.deepcopy(table)
    min_column = 0
    min_row = 0
    if len(order) == 0:
        answers_order = [0 for x in range(table.columns - 1)]
    else:
        answers_order = copy.deepcopy(order)    
    
    # find intersection
    
    min_item = 0
    
    for index, item in enumerate(table.matrix[table.rows - 1]):
        if index < table.columns - 1:
            if item < min_item:
                min_column = index
                min_item = item
    
    min_value = table.matrix[0][table.columns - 1] / table.matrix[0][min_column]
    
    for index, row in enumerate(table.matrix):
        if index < table.rows - 1:
            if row[table.columns - 1] / row[min_column] < min_value:
                min_value = row[table.columns - 1] / row[min_column]
                min_row = index
    
    answers_order[min_column] = min_row
    
    # form new table
    
    key_element = table.matrix[min_row][min_column] 
    
    new_table.matrix[min_row][min_column] = 1 / key_element     
    
    for i in range(new_table.rows):
        if i != min_row:
            new_table.matrix[i][min_column] = table.matrix[i][min_column] / key_element * (-1)
        
    for index, i in enumerate(table.matrix[min_row]):
        if index != min_column:
            new_table.matrix[min_row][index] = i / key_element   
            
    for i in range(table.rows):
        if i != min_row:
            for j in range(table.columns):
                if j != min_column:
                    new_table.matrix[i][j] = (table.matrix[i][j] * key_element - table.matrix[min_row][j] * table.matrix[i][min_column]) / key_element     
                    
    new_table.__str__() 
    print()  
    
    have_negative = False
    for item in new_table.matrix[new_table.rows - 1]:
        if item < 0:
            have_negative = True
            
    if have_negative:
        simplex_method(new_table, answers_order)
    else:
        income = new_table.matrix[table.rows - 1][table.columns - 1]
        
        for index, item in enumerate(answers_order):
            print(f'x{index + 1} = {new_table.matrix[item][table.columns - 1]}')
            
        print(f'MAX Income = {income}')    
                              

def main():
    print('---------------------\ncatalin software 2022\n---------------------')
    
    # origin_equtions = matrix_(4, 3)
    # origin_equtions.matrix = [[12, 4, 300], [4, 4, 120], [3, 12, 252], [-30, -40, 0]]
    
    amount_of_resourses = int(input('Enter amount of resourses: '))
    amount_of_products = int(input('Enter amount of products: '))
    
    origin_equtions = matrix_(amount_of_resourses + 1, amount_of_products + 1)
    
    for i in range(amount_of_resourses + 1):
        if i == amount_of_resourses:
            origin_equtions.matrix[i][amount_of_products] = 0
        else: 
            origin_equtions.matrix[i][amount_of_products] = int(input(f'Enter amount of {i + 1}\'s type stored resources: '))
        for j in range(amount_of_products):
            if i == amount_of_resourses:
                origin_equtions.matrix[i][j] = int(input(f'Enter price of {j + 1}\'s type product: '))  * (-1)
            else:    
                origin_equtions.matrix[i][j] = int(input(f'Enter amount of {i + 1}\'s type resources for produce {j + 1}\'s type product: '))  
                       
    origin_equtions.__str__()
    print()                   
    simplex_method(origin_equtions) 
       
if __name__ == "__main__":
    main()