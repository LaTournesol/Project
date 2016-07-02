import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.Stack;
import java.util.Queue;
import java.util.function.Function;

/**
 * Yue Liu, TianYang Jin
 * Extra Credit Options Implemented, if any:  (mention them here.)
 * 
 * Solution to Assignment 5 in CSE 373, Autumn 2014
 * University of Washington.
 * This assignment requires Java 8 JDK
 * 
 * There are totally 15 TODOs, please read the instructions carefully
 * and don't change the signature of the methods
 * 
 * Starter code provided by Steve Tanimoto and Si J. Liu, Nov. 21, 2014.
 *
 */

public class ExploredGraph {
	public final int NUMBER_OF_PEGS = 3; // number of pegs in this game
	private Set<Vertex> Ve; // collection of explored vertices
	private Set<Edge> Ee; // collection of explored edges
	private int VeSize; // size of collection of explored vertices
	private int EeSize; // size of collection of explored edges
	private List<Operator> operators; // collection of operators (6 in this game)
	private HashMap<Vertex, LinkedList<Edge>> map; // map of successor vertex with its edges
	private boolean ifBfs;
	public ExploredGraph() {
		initialize();
	}

	public void initialize() {
		Ve = new LinkedHashSet<Vertex>();
		Ee = new LinkedHashSet<Edge>();
		map = new HashMap<Vertex, LinkedList<Edge>>();
		VeSize = 0;
		EeSize = 0;
		ifBfs = false;
		setOperators();
	}
	
	// Initializes the field operators with 6 Operators;
	private void setOperators() {
		// TODO: Initialize the field operators with 6 Operators:
		// (i, j) = {(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)}
		operators = new ArrayList<Operator>();
		operators.add(new Operator(0, 1));
		operators.add(new Operator(0, 2));
		operators.add(new Operator(1, 0));
		operators.add(new Operator(1, 2));
		operators.add(new Operator(2, 0));
		operators.add(new Operator(2, 1));
	}

	public int nvertices() {
		return Ve.size();
	}

	public int nedges() {
		return Ee.size();
	}

	
	// Depth first search algorithm
	// Stop either reach the goal point or out of resource
	// use stack as data structure to determine the sequence
	// Records the visited vertex and edge, and add the vertex as the key, and its indegree as the value to the hashmap
	public void dfs(Vertex vi, Vertex vj) {
      System.out.println(" ------ Running DFS Search: ------ ");
		initialize();
		ifBfs = false;
		Stack<Vertex> vStack = new Stack<Vertex>();
		vStack.push(vi);
		Ve.add(vi);
		Vertex update = vi;
		while(!update.equals(vj) && !vStack.isEmpty()){
			Vertex next = vStack.pop();
			Ve.add(next);
			for(int i = 5; i >= 0; i--){
				Operator op = operators.get(i);
				if ((boolean)op.getPrecondition().apply(next)){
					Vertex start = new Vertex(next.toString());
					Vertex u = (Vertex)op.getTransition().apply(start);
					if (! Ve.contains(u)){
						vStack.push(u);
						Edge e = new Edge(next, u);
						Ee.add(e);
						if(!map.containsKey(u)){
							LinkedList<Edge> path = new LinkedList<Edge>();
							map.put(u, path);
						}
						map.get(u).add(e);
					}		
				}
			}
			update = vStack.peek();
		}
	}

	// Breath first search algorithm
	// us queue as data structure to determine the sequence
	// Records the visited vertex and edge, and add the vertex as the key, and its indegree as the value to the hashmap
	public void bfs(Vertex vi, Vertex vj) {
      System.out.println(" ------ Running DFS Search: ------ ");
	   initialize();
	   ifBfs = true;
	   Queue<Vertex> vQueue = new LinkedList<Vertex>();
	   vQueue.add(vi);
	   Ve.add(vi);
	   while(!vQueue.isEmpty()){
	   	Vertex next = vQueue.remove();
	   	for(int i = 0; i < 6; i++){
	   		Operator op = operators.get(i);
	   		if ((boolean)op.getPrecondition().apply(next)){
	   			Vertex start = new Vertex(next.toString());
	   			Vertex u = (Vertex)op.getTransition().apply(start);
	   			if (! Ve.contains(u)){
	   				Ve.add(u);
	   				vQueue.add(u);
	   				Edge e = new Edge(next, u);
	   				Ee.add(e);
	   				if(!map.containsKey(u)){
	   					LinkedList<Edge> path = new LinkedList<Edge>();
	   					map.put(u, path);
	   				}
	   				map.get(u).add(e);	
	   			}
	   		}
	   	}
	   }
}
	
	// retrieves the path to the goal vertex after call a search algorithm
	// returns a path as an array list
	public ArrayList<Vertex> retrievePath(Vertex vj) {
		ArrayList<Vertex> path = new ArrayList<Vertex>();
		path.add(vj);
		int count = 0;
		while(map.containsKey(vj)){
			LinkedList<Edge> temp = map.get(vj);
			Vertex prev;
			if(ifBfs){	
				prev = map.get(vj).get(0).vi;//uses the head of the hashmap
			}else{
				int size = map.get(vj).size();
				prev = map.get(vj).get(size - 1).vi;//uses the tail of the hashmap
			}
				path.add(prev);
				vj = prev;
		}
		for(int i = path.size() - 1; i > 0; i--){
			System.out.print(count + ": " + path.get(i).toString() + "--->");
			count++;
		}
      System.out.println(count + ": " + path.get(0).toString() + ".");
      System.out.println("Shortest Path Found, Path length = " + path.size());
		System.out.println();
		return path;
		
	}

	// return the shortest path between vi and vj, start from vi, end at vj
	// use breathfirst search algorithm as a search algorithm
	public ArrayList<Vertex> shortestPath(Vertex vi, Vertex vj) {
		bfs(vi, vj);
		this.ifBfs = true;
		int count = 0;
		ArrayList<Vertex> path = new ArrayList<Vertex>();
		path = retrievePath(vj);
		return path;
	}

	public Set<Vertex> getVertices() {
		return Ve;
	}

	public Set<Edge> getEdges() {
		return Ee;
	}


	public static void main(String[] args) {
		ExploredGraph eg = new ExploredGraph();
		// Test the vertex constructor:
		// Vertex v0 = eg.new Vertex("[[4,3,2,1],[],[]]");
		// System.out.println(v0);
		// Add your own tests here.
		// The autograder code will be used to test your basic functionality
		// later.
		Vertex v0 = eg.new Vertex("[[4,3,2,1],[],[]]");
		Vertex v1 = eg.new Vertex("[[],[],[4,3,2,1]]");
		eg.bfs(v0,v1);
		eg.retrievePath(v1);
		// eg.dfs(v0,v1);
		// eg.retrievePath(v1);
		// eg.shortestPath(v0, v1);
		
	}

	class Vertex {
		Stack<Integer>[] pegs; // Each vertex will hold a Towers-of-Hanoi state.

		// There will be 3 pegs in the standard version, but more if you do
		// extra credit option A5E1.
		
		// Constructor that takes a string such as "[[4,3,2,1],[],[]]":
		@SuppressWarnings("unchecked")
		public Vertex(String vString) {
			String[] parts = vString.split("\\],\\[");
			pegs = new Stack[NUMBER_OF_PEGS];
			for (int i = 0; i < NUMBER_OF_PEGS; i++) {
				pegs[i] = new Stack<Integer>();
				try {
					parts[i] = parts[i].replaceAll("\\[", "");
					parts[i] = parts[i].replaceAll("\\]", "");
					ArrayList<String> al = new ArrayList<String>(
							Arrays.asList(parts[i].split(",")));
					// System.out.println("ArrayList al is: " + al);
					Iterator<String> it = al.iterator();
					while (it.hasNext()) {
						Object item = it.next();
						// System.out.println("item is: " + item);
						Integer diskInteger = new Integer((String) item);
						pegs[i].push(diskInteger);
					}
				} catch (Exception e) {
				}
			}
		}

		//overrides the toString method
		public String toString() {
			String ans = "[";
			for (int i = 0; i < NUMBER_OF_PEGS; i++) {
				ans += pegs[i].toString().replace(" ", "");
				if (i < NUMBER_OF_PEGS - 1) {
					ans += ",";
				}
			}
			ans += "]";
			return ans;
		}

		@Override
		//Overrides the equals method
		public boolean equals(Object v) {
			if (this.hashCode() == ((Vertex) v).hashCode()) {
				return true;
			} else {
				return false;
			}
		}

		@Override
		//Overrides the hashCode method
		public int hashCode() {
			int hash = getHashCode();
			return hash;
		}
		
		private int getHashCode() {
			int disk1 = 0;
			int disk2 = 0;
			int disk3 = 0;
			if (!pegs[0].isEmpty()) {
				Stack<Integer> tempStack = new Stack<Integer>();
				int i = 0;
				while (!pegs[0].empty()) {
					int next = pegs[0].pop();
					disk1 = disk1 + next * (int)Math.pow (10, i);
					tempStack.push(next);
					i++;
				}
				while (!tempStack.isEmpty()) {
					pegs[0].push(tempStack.pop());
				}
			}
			if (!pegs[1].isEmpty()) {
				int i = 0;
				Stack<Integer> tempStack = new Stack<Integer>();
				while (!pegs[1].empty()) {
					int next = pegs[1].pop();
					disk2 = disk2 + next * (int)Math.pow (10, i);
					tempStack.push(next);
					i++;
				}
				while (!tempStack.isEmpty()) {
					pegs[1].push(tempStack.pop());
				}
			}
			if (!pegs[2].isEmpty()) {
				int i = 0;
				Stack<Integer> tempStack = new Stack<Integer>();
				while (!pegs[2].empty()) {
					int next = pegs[2].pop();
					disk3 = disk3 + next * (int)Math.pow (10, i);
					tempStack.push(next);
					i++;
				}
				while (!tempStack.isEmpty()) {
					pegs[2].push(tempStack.pop());
				}
			}
			int hashcode = disk1 * 11 + disk2 * 13 + disk3 * 19;
			return hashcode;
		}
	}

	
	class Edge {
		public Vertex vi;
		public Vertex vj;

		public Edge(Vertex vi, Vertex vj) {
			this.vi = vi;
			this.vj = vj;
		}

		public String toString() {
			return vi.toString() + " -> " + vj.toString();
		
			
		}

		@Override
		public boolean equals(Object e) {
			return this.hashCode() == ((Edge) e).hashCode();
		}

		@Override
		public int hashCode() {
			return this.toString().hashCode();
		}
	}

	class Operator {
		private int i, j;

		public Operator(int i, int j) {
			this.i = i;
			this.j = j;
		}

		// Additional explanation of what to do here will be given in GoPost or
		// as extra text in the spec.
		@SuppressWarnings("rawtypes")
		Function getPrecondition() {
			// return a function that can be applied to a vertex (provided
			// that the precondition is true) to get a "successor" vertex -- the
			// result of making the move.
			return new Function() {
				@Override
				public Object apply(Object vertex) {
					if(((Vertex) vertex).pegs[i].isEmpty()){
						return false;
					}else if(!((Vertex) vertex).pegs[j].isEmpty()){
						if(((Vertex) vertex).pegs[i].peek() < ((Vertex) vertex).pegs[j].peek()){
							return true;
						}else{
							return false;
						}
					}
					return true;
				}
			};
		}

		@SuppressWarnings("rawtypes")
		Function getTransition() {
			// should return a function that can be applied to a vertex
			// (provided that the precondition is true) to get a "successor"
			// vertex -- the result of making the move.
			return new Function() {
				@Override
				public Object apply(Object vertex) {
					Vertex newV = ((Vertex) vertex);
					newV.pegs[j].push(newV.pegs[i].pop());
					return newV;
				}
			};
		}

		public String toString() {
			return i + " --> " + j;
		}
	

	}
}



