import matplotlib.pyplot as plt 

# algo1 py
    # 4 nodes
    # 0.0009899139404296875
    # 10 nodes
    # 0.002051830291748047
    # 100 nodes
    # 0.11520624160766602
    # 200 nodes
    # 0.1848154067993164
    # 500 nodes
    # 2.6462483406066895
    # 1000 nodes
    # 4.4762483321020301

# algo1 cy
    # 4 nodes
    # 0.0009844303131103516
    # 10 nodes
    # 0.0024766921997070312
    # 100 nodes
    # 0.03609108924865723
    # 200 nodes
    # 0.1374516487121582
    # 500 nodes
    # 0.5514822006225586
    # 1000 nodes
    # 2.0404393672943115



# algo2 py
    # 4 nodes
    # 0.0006737709045410156
    # 10 nodes
    # 0.001325368881225586
    # 20 nodes
    # 0.003897428512573242
    # 50 nodes
    # 0.017029285430908203

    

# algo2 cy
    # 4 nodes
    # 0.0005385875701904297
    # 10 nodes
    # 0.0013756752014160156
    # 20 nodes
    # 0.004399299621582031
    # 50 nodes
    # 0.027696609497070312


# example how we create a graph for comparation 
# time = [0.0005385875701904297,0.0013756752014160156,0.004399299621582031, 0.027696609497070312]
# size =[4,10,20,50]
# plt.plot(size,time)
# plt.ylabel('Time')
# plt.xlabel('Size')
# plt.show()