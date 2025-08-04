import graphviz

# Create a Digraph object
dfa = graphviz.Digraph(format='png')
dfa.attr(rankdir='LR', size='10')

# Accepting states
accepting_states = {'S3', 'S4', 'S5', 'S10', 'S13', 'S17', 'S19', 'END', 'S0'}

# States
states = set([
    'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'END'
])

# Add nodes
for state in states:
    if state in accepting_states:
        dfa.node(state, shape='doublecircle')
    else:
        dfa.node(state)

# Initial state arrow
dfa.node('', shape='none')
dfa.edge('', 'S0')

# Transitions for tokens
transitions = {
    # Starting transitions
    ('S0', 'a', 'S1'),
    ('S0', 'b', 'S10'),
    ('S0', ' ', 'S0'),
    ('S0', 'c', 'END'),

    # a-starting tokens
    ('S1', 'a', 'S2'),
    ('S1', 'b', 'S3'),
    ('S1', ' ', 'S0'),
    ('S1', 'c', 'END'),

    ('S2', 'a', 'S4'),
    ('S2', 'b', 'S5'),
    ('S2', ' ', 'S0'),
    ('S2', 'c', 'END'),

    ('S3', ' ', 'S0'),
    ('S3', 'c', 'END'),

    ('S4', ' ', 'S0'),
    ('S4', 'c', 'END'),

    ('S5', ' ', 'S0'),
    ('S5', 'c', 'END'),
    ('S5', 'b', 'S18'),

    ('S18', 'a', 'S19'),
    ('S19', ' ', 'S0'),
    ('S19', 'c', 'END'),

    # b-starting tokens
    ('S10', 'a', 'S11'),
    ('S10', ' ', 'S0'),
    ('S10', 'c', 'END'),

    ('S11', 'a', 'S12'),
    ('S11', 'b', 'S14'),

    ('S12', 'b', 'S13'),
    ('S13', ' ', 'S0'),
    ('S13', 'c', 'END'),

    ('S14', 'a', 'S15'),
    ('S15', 'b', 'S16'),
    ('S16', 'a', 'S17'),
    ('S17', ' ', 'S0'),
    ('S17', 'c', 'END'),
}

# Add transitions to the graph
for start, label, end in transitions:
    dfa.edge(start, end, label=label)

# Render to file
dfa.render('dfa_scanner', view=True)  # Opens image viewer
