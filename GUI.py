import matplotlib.pyplot as plt
import numpy as np
from BubbleGraph import BubbleGraph as BG

class GUI():

    def __init__(self):
        self.matrix = None,
        self.n_row, self.n_col = None, None
        self.queue = None
        self.active_bubble = None

        self.color_dict = {
                           0: 'black',
                           1: 'blue',
                           2: 'red',
                           3: 'green',
                           4: 'yellow',
                           5: 'orange',
                           6: 'purple',
                           7: 'white'
                          }

    def load_queue(self, queue):
        # this can be a list of ints
        self.queue = queue

    def load_bubble(self,bubble):
        self.active_bubble = bubble

    def load_matrix(self,matrix):
        self.matrix = matrix
        self.n_row,self.n_col = matrix.shape[0],matrix.shape[1]
        
    def show(self,save_fig = False,fpath = None):

        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        mat_temp = np.flipud(self.matrix)

        # size the bubbles
        if self.n_col > self.n_row:
            bub_size = int(150000/self.n_col**2)
        else:
            bub_size = int(150000/self.n_row**2)

        empty_size = int(100/self.n_col)

        
        # show the grid
        for i in range(self.n_row):
            for j in range(self.n_col):

                # add in the offset
                if i % 2 == 1:
                    j_offset = j - .5
                else:
                    j_offset = j

                # change bubble size for empty locations
                if mat_temp[i,j] != 0:
                    size = bub_size
                else:
                    size = empty_size

                ax.scatter(j_offset,i,s= size,alpha = .7,
                            c = self.color_dict[mat_temp[i,j]])

        # show the active bubble
        size = bub_size
        ax.scatter(self.n_col//2,-2,
                    s = size,
                    alpha = .7,
                    c = self.color_dict[self.active_bubble])
        
        
        # show the queue
        size = bub_size/1.25
        ax.scatter(list(range((self.n_col-len(self.queue)),self.n_col)),
                    [-4]*len(self.queue),
                    s = size,
                    alpha = .7,
                    c = [self.color_dict[i] for i in self.queue])


        # format the plot
        ax.spines['bottom'].set_position(('data',-1))
        ax.spines['top'].set_position(('data',self.n_row))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['left'].set_bounds(-1,self.n_row)
        ax.spines['right'].set_bounds(-1,self.n_row)
        
        #save to file if saving
        if save_fig == True:
            plt.savefig(fpath)
            plt.close()
        else:
            fig.show()

            
    @staticmethod
    def test():
        
        matrix = BG.random_graph(10,10,5,2).matrix
        queue = [np.random.randint(1,6) for i in range(10)]
        active_bubble = 3
        print(matrix)
        gui = GUI()
        gui.load_matrix(matrix)
        gui.load_bubble(active_bubble)
        gui.load_queue(queue)
        # gui.show(save_fig = True,fpath = 'C:\\Users\\Steve\\Desktop\\test_image.jpg')
        gui.show()
