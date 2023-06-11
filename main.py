from non_binary_automaton import Automaton, State

# configuring all states
state1 = State(value='foo')
state2 = State(value='bar')
state3 = State(value='baz')

# adding transitions to the states
state1.add_transition('GOTO2', state2)
state1.add_transition('STAY1', state1)
state1.add_transition('GOTO3I', state3)
state2.add_transition('GOTO3', state3)

# configuring automaton
automaton = Automaton(states=[state1, state2, state3], initial_state=state1, accepting_state=state3)

belongs = automaton.is_accepted(['GOTO2', 'GOTO3'])
if belongs:
    print('values belongs to the automaton')
else:
    print('values don\'t belong to the automaton')

automaton.show_graph()
