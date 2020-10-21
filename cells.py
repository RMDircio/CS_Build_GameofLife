

class Cell:

    def __init__(self):
        ''' 
        set up cell to default of dead
        '''


    ### set up cell rules ###

    # set cell to off/dead
    def set_to_dead(self):
        '''
        Sets the cell to dead/off
        '''
        self._status = 'Dead'

    # set cell to on/alive
    def set_to_alive(self):
        '''
        Sets the cell to alive/on
        '''
        self._status = 'Alive'

    # is cell on/alive
    def cell_alive(self):
        '''
        Checks if cell is alive
        '''
        if self._status == 'Alive':
            return True
        return False

    # what grid should print
    def print_character(self):
        '''
        Determines what status of the cell that will be printed on the grid
        '''
        if self.cell_alive():
            return 'O'
        return '*'
 