#!/usr/bin/env python
# coding: utf-8

from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor

# simulator instance
sim = Aer.get_backend('qasm_simulator')

# circle creation:
# applying Hadamrd on every input qubit, and creating |-> state as input.
# creating function logic - "and between all qubits", and useing phase kickback
# applying Hadamrd on every ouput qubit
# measure qubit number 0
circs = []
for q_num in range(2,10):
    circ = QuantumCircuit((q_num*2),q_num)
    circ.h(0)
    for i in range(q_num-1):
        circ.h(1+(i*2))
    circ.x((q_num*2)-1)
    circ.h((q_num*2)-1)
    circ.barrier()
    for i in range(0,(q_num*2)-2,2):
        circ.ccx(i,i+1,i+2)
    circ.cx((q_num*2)-2,(q_num*2)-1)
    for i in range((q_num*2)-2,0,-2):
        circ.ccx(i-2,i-1,i)
    circ.barrier()
    circ.h(0)
    for i in range(q_num-1):
        circ.h(1+(i*2))
    circ.measure(0,0)
    circs.append(circ)

circs[1].draw()

# running each circle 1 Million times
results = []
for circ in circs:
    res = execute(circ,backend=sim, shots=1024*1024).result()
    results.append(res)

plot_histogram(results[1].get_counts())
plot_histogram(results[1].get_counts())
plot_histogram(results[2].get_counts())
plot_histogram(results[3].get_counts())
plot_histogram(results[4].get_counts())
plot_histogram(results[5].get_counts())
plot_histogram(results[6].get_counts())
plot_histogram(results[7].get_counts())
