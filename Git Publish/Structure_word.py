class node: # chain table
		def __init__(self,var):
			self.var_start=var[0]
			self.var_end=var[1]
			self.next=None
			self.prev=None #needed to identify the 1st Node
			
def parse(str):
	return str[0],str[2]


final_output=""

def recursive_read(n):
	global final_output 
	final_output = final_output + n.var_start
	if n.next == None:
		final_output = final_output + n.var_end
	else:
		recursive_read(n.next)
	
	return None

all_nodes = []

for substr in ["I>N","A>I","P>A","S>P"]:
	all_nodes.append(node(parse(substr)))

for loop_node in all_nodes:
	for next_node in all_nodes:
		if loop_node.var_end == next_node.var_start:
			loop_node.next = next_node
			next_node.prev=loop_node

for loop_node in all_nodes:
	if loop_node.prev==None:
		start=loop_node

recursive_read(start)

print (final_output)