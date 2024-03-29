import numpy as np
X=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)
X=X/np.amax(X,axis=0)
y=y/100
def sigmoid(x):
    return 1/(1+np.exp(-x))
def derivatives_sigmoid(x):
    return x*(1-x)
epoch=5000
lr=0.1
inputlayer_neurons=2
hiddenlayer_neurons=3
output_neurons=1
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons,))
bout=np.random.uniform(size=(1,output_neurons,))
for i in range(epoch):
    hinpl=np.dot(X,wh)
    hinp=hinpl+bh
    hlayer_act=sigmoid(hinp)
    outinpl=np.dot(hlayer_act,wout)
    outinp=outinpl+bout
    output=sigmoid(outinp)
    EO=y-output
    outgrad=derivatives_sigmoid(output)
    d_output=EO*outgrad
    EH=d_output.dot(wout.T)
    hiddengrad=derivatives_sigmoid(hlayer_act)
    d_hiddenlayer=EO*hiddengrad
    wout+=hlayer_act.T.dot(d_output)*lr
    wh+=X.T.dot(d_hiddenlayer)*lr
print("INPUT:\n" +str(X))
print("Actual output:\n" +str(y))
print("Predicted output:\n",output)
#INPUT:
#[[0.66666667 1.        ]
# [0.33333333 0.55555556]
# [1.         0.66666667]]
#Actual output:
#[[0.92]
# [0.86]
# [0.89]]
#Predicted output:
# [[0.89555526]
# [0.87946911]
# [0.8949651 ]]
​#