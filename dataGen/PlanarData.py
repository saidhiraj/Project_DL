import numpy as np
import planarity
import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(10)
e = np.array(G.edges)
X,y = [],[]
count = 0;
for i in range(10000):
    idx= np.random.choice(len(e),21);
    edg = e[idx];
    G = nx.empty_graph(10);
    G.add_edges_from(edg)
    mat = np.zeros((10,10),dtype=int);
    for i in edg:
        mat[tuple(i)]=True;
        mat[tuple(i[::-1])]=True;
    X.append(mat.reshape(1,-1)[0]);
    #print(mat)

    planar = planarity.is_planar(G)
    if(planar):
        label = 1
        #print(i,label)
    else:
        label = 0
    #nx.draw(G);
    #plt.show();

    y.append(int(label))
    count += label
    #print(i,label)
    
y = np.asarray(y)
X = np.asarray(X)
import pickle
pickle_out = open('planar.pickle','wb')
pickle.dump((X,y),pickle_out);
pickle_out.close();
pickle_in  = open('planar.pickle','rb')
X,y = pickle.load(pickle_in);
print(type(X),type(X[0][0]))
print("X shape",len(X),X[0].shape)
print("y shape",len(y))

print("DONE")
print("# Planar :",count)
