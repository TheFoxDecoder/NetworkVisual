from dataclasses import dataclass
BLOCK4 = 65536
BLOCK8 = BLOCK4**BLOCK4

@dataclass
class DataNetwork:
    nodes: int
    connections: int
    connection_spaces: int
    node_spaces: int
    tot_space: int


# all the data capacity represnened in KB (KiloBytes)
class NeuronConnectionCalcuator:
    # @brief  this class use for the fundermential of the neuron connection info calculation
    # @param nodes amount of the total nodes
    # @param conn_ratio always add as 1 : conn_ratio
    def __init__(self,nodes=BLOCK4,conn_ratio=16):
        self.nodes = nodes
        self.conn_ratio = conn_ratio
        self.dt = DataNetwork(
            nodes=self.nodes,
            connections=self.calculate_connections(),
            connection_spaces=0,  # You may update this value accordingly
            node_spaces=0,         # You may update this value accordingly
            tot_space=0            # You may update this value accordingly
        )
        self.run()
    
    @classmethod
    def data(self):
        return self.dt
    
    @classmethod
    def run(self):
        self.dt.connections = self.nodes/ self.conn_ratio
        self.dt.connection_spaces = self.dt.connections*16  # 16 is holding two memory address  as in linked-list
        self.dt.node_spaces = self.nodes * 8               # 8 as in KB
        self.dt.tot_space = self.dt.connection_spaces + self.dt.node_spaces
    
