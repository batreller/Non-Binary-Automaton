# Non-Binary Automaton

**This project implements a non-binary automaton that can process a list of values and determine whether or not it belongs to the automaton's language.**

# Code Example

```
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
```

### In case above, values belongs to the automaton, and graph looks like that

![graph image](https://i.imgur.com/Q6gIpru.png)
# Overview
**The non-binary automaton is defined by a set of states, a set of input symbols, a transition function, an initial state, and a set of final states. The automaton processes a list of values and transitions from state to state based on the input values.**

# Resources

**Here are some resources you may find helpful to learn more about non-binary automata:**

**[Automata Theory](https://en.wikipedia.org/wiki/Automata_theory) - Wikipedia article on Automata Theory**

**[Introduction to the Theory of Computation](https://www.amazon.com/Introduction-Theory-Computation-Michael-Sipser/dp/113318779X) by Michael Sipser - A comprehensive book on the theory of computation and automata**

**Feel free to modify the above template to suit your project's specific needs. Make sure to include relevant sections such as installation instructions, usage examples, and any additional resources that may be helpful for users.**
