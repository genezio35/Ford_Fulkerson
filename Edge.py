class Edge:
    def __init__(self, _source, _destination, _flow):
        self.source = _source
        self.destination = _destination
        self.flow = _flow
        self.actual_flow = self.flow

    def resetWeight(self):
        self.actual_flow = self.flow

    def lowerFlow(self, lowering_by):
        self.actual_flow -= lowering_by

    def __str__(self):
        return f'Edge to {self.destination} with actual flow = {self.actual_flow}'
