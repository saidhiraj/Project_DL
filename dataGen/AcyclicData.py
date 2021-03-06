import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(10)
e = np.array(G.edges)
X,y = [],[]
count = 0;
for i in range(10000):
    idx= np.random.choice(len(e),8);
    edg = e[idx];
    G = nx.empty_graph(10);
    G.add_edges_from(edg)
    mat = np.zeros((10,10),dtype=int);
    for j in edg:
        mat[tuple(j)]=True;
        mat[tuple(j[::-1])]=True;
    X.append(mat.reshape(1,-1)[0]);
    #print(mat)

    label = any(nx.cycle_basis(G))
    y.append(int(label))
    count += label
    print(i,label)
    #nx.draw(G);
    #plt.show();

y = np.asarray(y)
X = np.asarray(X)
import pickle
pickle_out = open('acyclic.pickle','wb')
pickle.dump((X,y),pickle_out);
pickle_out.close();

print("X shape",len(X),X[0].shape)
print("y shape",len(y))

print("DONE")
print("# Cycle:",count)
