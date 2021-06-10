import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from([('1', {'label': 'Person', 'name': 'Raj', 'age': 24,  'Gender': 'Male'}),
                  ('2', {'label': 'Person', 'name': 'Mohan', 'age': 30,'Gender': 'Male'}),
                  ('3', {'label': 'Person', 'name': 'Maya', 'age': 30, 'Gender': 'Female'}),
                  ('4', {'label': 'Person', 'name': 'Swati', 'age': 30,'Gender': 'Female'}),
                  ('5', {'label': 'Person', 'name': 'Riya', 'age': 30, 'Gender': 'Female'}),
                  ('6', {'label': 'Person', 'name': 'Hema', 'age': 34, 'Gender': 'Male'})])



G.add_node('7', label='Event', name='Cricket World Cup')
G.add_node('8', label='Event', name='Football World Cup')
G.add_node('9', label='Event', name='Olympics')
G.add_node('10', label='Event', name='GAPD')
G.add_node('10', label='Event', name='AWSome Day')
G.add_node('11', label='Event', name='Fun Music Symposium')

G.add_node('12', label='Category', name='Sports')
G.add_node('13', label='Category', name='Education')
G.add_node('14', label='Category', name='Music')

G.add_edges_from([('7', '12'), ('8', '12'), ('9', '12'),('9', '13'), ('10', '13'), ('11', '14')],
                 type='IS_PART_OF_CATEGORY')

G.add_edges_from([('1', '7'), ('1', '10'), ('1', '11'),('2', '8'), ('2', '19'), ('2', '11'),
                  ('3', '7'), ('3', '10'), ('4', '11'),('4', '8'), ('5', '19'), ('6', '11')],
                 type='Attended')

G.add_edges_from([('1', '2'), ('1', '4'), ('1', '3'),('2', '3'), ('2', '5'), ('2', '6'),
                  ('3', '5'), ('3', '6'), ('4', '5'),('4', '2'), ('5', '6'), ('6', '1')],
                 type='Friends')

G.add_node('15', label='SocialMedia',  name='Facebook')
G.add_node('16', label='SocialMedia',  name='Twitter')
G.add_node('17', label='SocialMedia',  name='Instagram')
G.add_node('18', label='SocialMedia',  name='LinkedIn')
G.add_node('19', label='SocialMedia',  name='YouTube')


G.add_edges_from([('1', '15'), ('1', '16'), ('1', '19'), ('3', '19'),
                  ('2', '19'), ('2', '17'), ('3', '15'),
                   ('4', '15'), ('4', '16'), ('5', '15'),
                    ('5', '19'), ('6', '16'), ('6', '18')],
                 type='HAS_ACCOUNT')

#print(G.nodes)
#print(G.edges)

pos = nx.spring_layout(G)

nx.draw(G, pos)
node_labels = nx.get_node_attributes(G, 'name')
nx.draw_networkx_labels(G, pos, labels=node_labels)

plt.show()
