from typing import List, Any
import networkx as nx
import matplotlib.pyplot as plt
from .state import State


class Automaton:
    def __init__(self, states: List[State], initial_state=None, accepting_state=None):
        """
        represents non binary automaton with all states and conditions

        :param states: a list of all states with all transitions
        :param initial_state: initial state, if None then 0 element of states is an initial state
        :param accepting_state: accepting state, if None then -1 element of states is an accepting state
        """

        if initial_state is None:
            initial_state = states[0]
        if accepting_state is None:
            accepting_state = states[-1]

        self.states = states  # a list of states
        self.initial_state = initial_state  # initial state
        self.accepting_state = accepting_state  # accepting state
        self.current_state = initial_state  # current state

    def is_accepted(self, values: List[Any]) -> bool:
        """
        validate a list of values
        :param values: a list of values to validate
        :return: if the input values belongs to the language of the automaton
        :rtype: bool
        """

        for value in values:
            self.current_state = self.current_state.next_state(value)

        # using `==` instead of `is` will cause incorrect working of the program
        # because it will return True if current state is the same as accepting
        # but it doesn't guarantee that current state is accepting state (we may have 2 same states for example)
        if self.current_state is self.accepting_state:
            return True
        return False

    def show_graph(self):
        # initialization of graph
        graph = nx.DiGraph()

        # add nodes to the graph
        for state in self.states:
            graph.add_node(str(state.value))

        # add transitions to the graph
        for state in self.states:
            for symbol, next_state in state.transitions.items():
                graph.add_edge(str(state.value), str(next_state.value), label=symbol)

            if state in state.transitions.values():
                graph.add_edge(str(state.value), str(state.value), label="self")

        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold', arrows=True)
        edge_labels = nx.get_edge_attributes(graph, 'label')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')

        plt.title("non binary automaton")
        plt.show()
