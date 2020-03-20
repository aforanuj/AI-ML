g = {}
n = 500
while n!=0:
   n = int(input("\n 0. Exit\n 1. Create Node\n 2. Add Edges\n 3. Delete Node\n 4. Delete Edge \n5. Print Graph\n 6.BFS\n"))

   if n == 1:
        keys = int(input())
        g[keys] = []
        print("Node Added !!!!!")

   elif n == 2:
       print("Starting Vertex : ")
       keys = int(input())
       print("Ending Vertex : ")
       ed = int(input())
       g[keys].append(ed)
       print("Edge Added !!!!!")

   elif n == 3:
       print("Delete Node : ")
       del_node = int(input())
       del g[del_node]
       print("Node Deleted !!!!!")
   elif n==4:
       del_edge = int(input("Enter Edge you want to delete:"))
       for x,y in g.items():
            g[x].remove(del_edge)

       print("Edge Deleted !!!!!")

   elif n == 5:
       print(g)
   elif n == 6:
       visited={x:False for x in g}
       s = int(input("Enter Starting Node"))
       queue = []
       queue.append(s)

       visited[s] = True
       while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in g[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
